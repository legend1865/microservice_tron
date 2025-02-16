from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_PORT: int

    MONGO_HOST: str
    MONGO_PORT: int
    MONGO_NAME: str

    model_config = SettingsConfigDict(env_file="certs/.env", env_nested_delimiter="__")

    @property
    def db_url_async(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


setting = Settings()
