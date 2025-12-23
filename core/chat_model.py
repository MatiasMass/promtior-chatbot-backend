from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI

def llm_model(model, chat_model):

    if model == "ollama":
        return ChatOllama(
            model=chat_model,
            validate_model_on_init=True,
            temperature=0.2
        )
    elif model == "gemini":
        return ChatGoogleGenerativeAI(
            model=chat_model,
            temperature=0.2,  # Gemini 3.0+ defaults to 1.0         
            max_output_tokens=1024   
        )

