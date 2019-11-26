from dotenv import load_dotenv

load_dotenv()

import os

TOKEN = os.getenv("TOKEN")
WEATHER_URL = os.getenv("WEATHER_URL")
