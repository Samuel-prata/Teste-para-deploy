import os
from dotenv import load_dotenv

load_dotenv()  # Carrega o .env na variável


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_PROD')
