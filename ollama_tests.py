from ollama import chat
from ollama import ChatResponse


# stream = chat(
#     model="llama3.2",
#     messages=[{"role": "user", "content": "Why is the sky blue?"}],
#     stream=True,
# )

# for chunk in stream:
#     print(chunk["message"]["content"], end="", flush=True)

# import asyncio
# from ollama import AsyncClient


# async def chat():
#     message = {"role": "user", "content": "Why is the sky blue?"}
#     async for part in await AsyncClient().chat(
#         model="llama3.2", messages=[message], stream=True
#     ):
#         print(part["message"]["content"], end="", flush=True)


# asyncio.run(chat())

import ollama

data = ollama.embed(
    model="llama3.2", input="The sky is blue because of rayleigh scattering"
)

print(data)
