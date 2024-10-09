import ngrok
import logfire
import uvicorn
import os
import asyncio
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

load_dotenv()

NGROK_AUTH_TOKEN = os.getenv("NGROK_AUTHTOKEN")
APPLICATION_PORT = 5000

logfire.configure()

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logfire.info("Starting application")
        ngrok.set_auth_token(NGROK_AUTH_TOKEN)
        ngrok.forward(addr = APPLICATION_PORT, domain = "cleanly-thankful-calf.ngrok-free.app")
        yield
        logfire.info("Shutting down application")
    except Exception as e:
        logfire.error(f"Lifespan error: {e}")
    finally:
        logfire.info("Shutting down application")
        ngrok.disconnect()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    logfire.info("Hello bananana")
    return {"message": "Hello bananana"}

# https://medium.com/@atulkumar_68871/building-a-streaming-speech-to-text-application-with-fastapi-and-amazon-transcribe-6203d857375a
@app.websocket("/TranscribeStreaming")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    websocket_open = True
    stop_audio_stream = False
    audio_queue = asyncio.Queue()
    try:
        while True:
            data = await websocket.receive()
            if data["type"] == "websocket.recieve":
                if "bytes" in data:
                    audio_chunk = data["bytes"]
                    await audio_queue.put(audio_chunk)
                elif "text" in data:
                    text_message = data["text"]
                    if text_message == "submit_response":
                        stop_audio_stream = True
                        break
    except WebSocketDisconnect:
        websocket_open = False
        await websocket.close()


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=APPLICATION_PORT, reload=True)
