import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import HumanMessage
from core.chat_model import llm_model
from services.pdf import get_data_from_pdf
from core.system_prompt import SYSTEM_PROMPT

load_dotenv()

CONTEXT_DATA_PDF = get_data_from_pdf()
FORMATTED_SYSTEM_PROMPT = SYSTEM_PROMPT.format(context=CONTEXT_DATA_PDF)

#model = "ollama"
#chat_model = "gemma3:12b"
model = "gemini"
chat_model = "gemini-2.5-flash"

llm = llm_model(model, chat_model)

# --- 2. Creación del Agente ---
checkpointer = InMemorySaver()

# Usamos create_agent que es el estándar actual
agent = create_agent(
    model=llm,
    system_prompt=FORMATTED_SYSTEM_PROMPT,
    # response_format=ToolStrategy(ResponseFormat),
    checkpointer=checkpointer
)

# --- 3. Función del Chatbot para WebSocket ---
async def run_chatbot(message: str):
    config = {"configurable": {"thread_id": "1"}}
    
    # IMPORTANTE: Invocamos al AGENTE, no a una cadena manual
    # El agente ya sabe usar el prompt, las herramientas y el LLM
    inputs = {"messages": [HumanMessage(content=message)]}
    
    # Usamos stream para que sea compatible con el WebSocket
    async for event in agent.astream(inputs, config=config, stream_mode="values"):
        last_message = event["messages"][-1]
        # Retornamos solo el contenido del último mensaje generado
        # print(event)
        if model == "gemini":
            response_text = last_message.text
        else:
            response_text = last_message.content
        
    return response_text