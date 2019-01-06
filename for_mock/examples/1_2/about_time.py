# about_time.py

from datetime import datetime

from utils import get_today_info


def is_today_my_birthday(birthday):
    month, day = get_today_info()

    try:
        birthday = datetime.strptime(birthday, "%m-%d")
    except Exception as e:
        raise ValueError(str(e))

    if month == birthday.month and day == birthday.day:
        return True
    return False