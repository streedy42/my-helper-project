from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_service import ask_gpt

router = APIRouter()

# 데이터 검증
class ChatRequest(BaseModel):
    question: str

@router.post("/")
async def chat(request: ChatRequest):
    answer = await ask_gpt(request.question)
    return {"answer": answer}