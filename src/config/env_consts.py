import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_HOST = os.environ.get('DATABASE_ENGINE')
DATABASE_ENGINE = os.environ.get('DATABASE_ENGINE')
DATABASE_NAME = os.environ.get('DATABASE_NAME')

ENV_CONSTS = {
    'SECRET_KEY': SECRET_KEY,
    'DATABASE_URI': f'{DATABASE_ENGINE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}',
}
