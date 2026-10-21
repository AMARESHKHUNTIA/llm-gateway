
from fastapi import FastAPI

from app.schemas import ChatRequest, ChatResponse
from app.llm_client import generate_response

app = FastAPI(title="My First LLM Gateway")


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    answer = await generate_response(request.prompt)

    return ChatResponse(answer=answer)
