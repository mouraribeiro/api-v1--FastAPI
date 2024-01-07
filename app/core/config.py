from typing import List
from decouple import config
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY",cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY",cast=str)
    # ALGORITHM = "HS256"
    ACESS_TOKEN_EXPIRE_MINUTES:int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES:int = 60 * 24 * 7 #7 dias
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl]=[]
    PROJECT_NAME:str =  "APIFAST"



    #DATABASE


    MONGO_CONNECTION_STRING:str = config("MONGO_CONNECTION_STRING", cast = str)
    class Config:
        case_Sensitive = True

settings = Settings()