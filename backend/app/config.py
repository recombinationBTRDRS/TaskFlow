from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql+asyncpg://taskflow:password@localhost:5432/taskflow_db"
    
    # API
    api_prefix: str = "/api"
    debug: bool = True
    
    # Security
    secret_key: str = "your-secret-key-change-in-production"
    
    # CORS
    allowed_origins: list[str] = ["http://localhost:3000"]
    
    class Config:
        env_file = ".env"

settings = Settings()