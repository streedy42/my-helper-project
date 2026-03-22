from fastapi import FastAPI
from app.api.endpoints import chat
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# 라우터 연결 (앞에 /chat 이 붙도록 설정)
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

@app.get("/")
def index():
    return {"status": "running", "message": f"Welcome to {settings.PROJECT_NAME}"}

# 서버 시작 시 업로드 폴더가 없으면 생성
settings.UPLOAD_DIR.mkdir(exist_ok=True)