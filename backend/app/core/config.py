from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    PROJECT_NAME: str = "My Helper Project"
    OPENAI_API_KEY: str
    
    # 현재 파일(config.py) 위치 기준으로 프로젝트 루트(backend) 경로 계산
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
    UPLOAD_DIR: Path = BASE_DIR / "uploads"

    class Config:
        env_file = ".env"

settings = Settings()