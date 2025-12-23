# Usamos una imagen ligera de Python
FROM python:3.12-slim

# Evitar que Python genere archivos .pyc y permitir logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copiar archivos de dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Exponer el puerto de FastAPI
EXPOSE 8080

# Comando para correr la app con Uvicorn
# Usamos la sintaxis de shell para que pueda leer la variable de entorno
# ${PORT:-8000} significa: "Usa el puerto que me de Railway, si no hay ninguno, usa 8000"
CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}