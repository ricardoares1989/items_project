from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    github_token: str = Field(default="")
    openai_api_key: str = Field(default="")
    db_host: str = Field(default="localhost")
    db_name: str = Field(default="postgres")
    db_port: int = Field(default=5432)
    db_user: str = Field(default="postgres")
    db_pass: str = Field(default="postgres")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
