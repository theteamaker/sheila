from dotenv import load_dotenv

load_dotenv()

import os

TOKEN = os.getenv("TOKEN")
WEATHER_URL = os.getenv("WEATHER_URL")
IMAGE_STORE_URL = os.getenv("IMAGE_STORE_URL")
SQL_DATABASE = os.getenv("SQL_DATABASE")
