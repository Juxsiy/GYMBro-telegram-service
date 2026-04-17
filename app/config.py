from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"

    AI_SERVICE_URL: str
    STATISTICS_SERVICE_URL: str

    TELEGRAM_BOT_TOKEN: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()