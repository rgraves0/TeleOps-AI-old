from config import TELEGRAM_ADMIN_ID

def authorized(user_id: int):
    return user_id == TELEGRAM_ADMIN_ID
