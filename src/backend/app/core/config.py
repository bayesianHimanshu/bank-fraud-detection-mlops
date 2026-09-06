from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

# config.py -> core -> app -> backend -> src -> repo root
BASE_DIR = Path(__file__).resolve().parents[4]

class Settings(BaseSettings):
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"

    API_V1_STR: str
    PROJECT_NAME: str
    PROJECT_DESCRIPTION: str
    SITE_NAME: str
    DATABASE_URL: str = ""

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".envs" / ".env.local",
        env_ignore_empty=True,
        extra="ignore",
    )

settings = Settings()
