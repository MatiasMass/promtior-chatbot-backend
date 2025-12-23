from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import promtior_chatbot

app = FastAPI()


@app.get("/")
def hello_world():

    return {"message": "hello world!"}

@app.get("/info/")
def get_info():
    """Provide information of this project"""

    info = {
        "author": "Matías Mass",
        "age": 26,
        "nacionality": "Argentina"
    }

    return info

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:

            data = await websocket.receive_text() 
            print(data)
            # Lógica de LangChain aquí...
            response = await promtior_chatbot.run_chatbot(data)
            print(response)
            await websocket.send_text(f"{response}")
            
    except WebSocketDisconnect:
        # Aquí capturamos la desconexión (Código 1001 o 1000)
        print("Cliente desconectado normalmente")
        
    except Exception as e:
        # Aquí capturamos cualquier otro error inesperado
        print(f"Error inesperado: {e}")