import os

from pydantic_settings import BaseSettings, SettingsConfigDict

from dotenv import load_dotenv

load_dotenv()
class Settings(BaseSettings):

    DB_BRAND:str =os.environ.get("DB_BRAND")
    DB_ENGINE:str = os.environ.get("DB_ENGINE")
    DB_USER:str = os.environ.get("DB_USER")
    DB_PASSWORD:str= os.environ.get("DB_PASSWORD")
    DB_HOST:str= os.environ.get("DB_HOST")
    DB_PORT:int= os.environ.get("DB_PORT")
    DB_NAME:str= os.environ.get("DB_NAME")

    @property
    def database_url(self):

        return (
            f"{self.DB_BRAND}+{self.DB_ENGINE}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}"
            f":{self.DB_PORT}/{self.DB_NAME}"
        )

    # model_config = SettingsConfigDict(env_file=".env", extra="ignore")

