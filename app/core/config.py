import os
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    app_name: str ="Schrimp APP"
    ENV: str = os.getenv("ENV", "production")
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    mongodb_user: str = "admin"
    mongodb_password: str = "admin"
    mongodb_host: str = "localhost"
    mongodb_port: int = 27017
    mongodb_name: str = "schrimp-api"
    JWT_SECRET_KEY: str = "fastapi"
    JWT_ALGORITHM: str = "HS256"


    @property
    def mongodb_url(self):
        return f"mongodb://{self.mongodb_user}:{self.mongodb_password}@{self.mongodb_host}:{self.mongodb_port}/{self.mongodb_name}"

    class Config:
        env_file = ".env"


config = Config()

