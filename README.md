
# Objetivo de la Documentación
El propósito de esta documentación es proporcionar una visión general completa del enfoque arquitectónico, los detalles de implementación y la pila tecnológica utilizada para construir el Promtior AI Chatbot. Este informe permite una evaluación detallada de la escalabilidad, la seguridad y la integración de los patrones RAG (Recuperación-Generación Aumentada) de la solución.

## Resumen del Proyecto
### El Enfoque
Mi objetivo era desarrollar un chatbot listo para producción que no solo "chateara", sino que actuara como una fuente confiable de información para Promtior. Abordé el reto implementando una arquitectura RAG Agentic. En lugar de una simple cadena lineal, utilicé LangGraph para crear un agente con reconocimiento de estado capaz de mantener el historial de conversaciones y procesar el contexto de múltiples fuentes simultáneamente.

### Lógica de Implementación
Inyección de Contexto (RAG): Desarrollé un sistema de ingesta de doble fuente. El backend extrae texto del PDF técnico oficial y extrae datos en tiempo real del sitio web de Promtior mediante WebBaseLoader.

- El "Cerebro": Elegí Gemini 2.5 Flash para la implementación en producción debido a su enorme ventana de contexto y sus capacidades de razonamiento, manteniendo Ollama (Gemma 3) como alternativa de desarrollo local.
- Experiencia en tiempo real: Para garantizar una experiencia de usuario moderna, implementé la transmisión asíncrona mediante WebSockets. Esto permite que el modelo transmita tokens al frontend de React a medida que se generan, minimizando la latencia percibida.
- Gestión de estado: Utilizando InMemorySaver de LangGraph, implementé un sistema de memoria basado en hilos que permite al bot seguir preguntas complejas de seguimiento.

### Principales desafíos y soluciones
- El "Muro" de la implementación: Uno de los mayores obstáculos fue implementar un backend de Python/LangChain en Railway mientras se mantenía un frontend de React en un host diferente. Lo resolví configurando políticas CORS estrictas y gestionando la inyección dinámica de puertos en Docker para garantizar la seguridad del protocolo de enlace de WebSockets (wss://).
- Colisión de contexto: Inicialmente, el modelo tuvo dificultades para priorizar la información. Solucioné esto refinando el indicador del sistema con estrictas "barreras de seguridad", impidiendo que el modelo usara datos de entrenamiento externos y obligándolo a ceñirse estrictamente al {context} proporcionado.
- Seguridad de dependencias: Durante la implementación, Railway bloqueó la compilación debido a vulnerabilidades en paquetes heredados. Realicé una auditoría de seguridad y actualicé el proyecto a Next.js 15.0.7 (y versiones equivalentes de Vite) para cumplir con los estándares de seguridad de producción.

## Información relevante:
- https://docs.langchain.com/oss/python/langchain/quickstart
- https://docs.langchain.com/oss/python/langchain/rag#loading-documents
- https://docs.langchain.com/oss/python/integrations/chat/ollama
- https://docs.langchain.com/oss/python/integrations/splitters
- https://docs.langchain.com/oss/javascript/integrations/providers/google
- https://docs.langchain.com/oss/python/langchain/streaming
