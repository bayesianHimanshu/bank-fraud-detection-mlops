import os
from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

# config.py -> core -> app -> backend -> repo root
BASE_DIR = Path(__file__).resolve().parents[3]

# In containers the env vars are injected by compose (env_file), so the dotenv
# file may be absent; pydantic-settings simply ignores a missing env_file.
ENV_FILE = Path(os.getenv("ENV_FILE", BASE_DIR / ".envs" / ".env.local"))

class Settings(BaseSettings):
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"

    API_V1_STR: str
    PROJECT_NAME: str
    PROJECT_DESCRIPTION: str
    SITE_NAME: str
    DATABASE_URL: str = ""

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_ignore_empty=True,
        extra="ignore",
    )

settings = Settings()
