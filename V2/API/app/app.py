from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from ollama import AsyncClient

app = FastAPI()


async def local_chat():
    message = {"role": "user", "content": "Hello?"}
    async for part in await AsyncClient().chat(
        model="llama3.2", messages=[message], stream=True
    ):
        # print(part["message"]["content"], end="", flush=True)
        yield part["message"]["content"]


@app.get("/stream")
async def main():
    return StreamingResponse(local_chat(), media_type="text/event-stream")


# asyncio.run(local_chat())
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
