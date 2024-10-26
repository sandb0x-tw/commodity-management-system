# pylint: disable=too-few-public-methods

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_HOST = os.getenv('DB_HOST')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')

    JWT_SECRET = os.getenv('JWT_SECRET')

    DEBUG = False
    ALLOW_CORS = False

class DevelopmentConfig(Config):
    DEBUG = True
    ALLOW_CORS = True

def get_runtime_config():
    return os.getenv("RUNTIME_CONFIG", "Development")
