from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:admin@localhost:5432/database"

    SECRET_KEY: str = "change_this_to_a_secure_secret_key"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_TIME: int = 3600

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()