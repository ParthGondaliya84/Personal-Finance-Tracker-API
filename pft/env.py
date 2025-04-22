import os
import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env.str('SECRET_KEY')

DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["127.0.0.1", "localhost"])


# Database Details
PFT_DB_NAME = env.str('PFT_DB_NAME')
PFT_DB_USER = env.str('PFT_DB_USER')
PFT_DB_PASSWORD = env.str('PFT_DB_PASSWORD')
PFT_DB_HOST = env.str('PFT_DB_HOST')
PFT_DB_PORT = env.int('PFT_DB_PORT', default=5432)

