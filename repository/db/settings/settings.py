from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    DB_BRAND: str
    DB_ENGINE: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    @property
    def database_url(self):

        return (
            f"{self.DB_BRAND}+{self.DB_ENGINE}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}"
            f":{self.DB_PORT}/{self.DB_NAME}"
        )

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
