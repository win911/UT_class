# utils.py

from datetime import datetime


def get_today_info():
    today = datetime.utcnow()
    return today.month, today.day