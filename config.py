from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    MODE: str
    MONGO_HOST: str
    MONGO_PORT: int
    MONGO_NAME: str

    model_config = SettingsConfigDict(env_file="certs/.env", env_nested_delimiter="__")


setting = Settings()
