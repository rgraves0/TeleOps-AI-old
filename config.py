import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_ADMIN_ID = int(os.getenv("TELEGRAM_ADMIN_ID"))
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
APP_URL = os.getenv("APP_URL")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
