# app/config.py

from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "MAO System"
    DEBUG: bool = True

    MODEL_NAME: str = "mistral"
    MODEL_PROVIDER: str = "ollama"  
    OPENAI_API_KEY: str | None = None

    
    TAVILY_API_KEY: str | None = None

  
    VECTOR_DB_PATH: str = "data/faiss_index"
    GRAPH_DB_URI: str = "bolt://localhost:7687"
    GRAPH_DB_USER: str = "neo4j"
    GRAPH_DB_PASSWORD: str = "password"

    
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    
    MAX_AGENT_ITERATIONS: int = 5
    MAX_CONTEXT_LENGTH: int = 4000


    model_config = SettingsConfigDict(
        env_file=".env",          # load from .env
        env_file_encoding="utf-8",
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()