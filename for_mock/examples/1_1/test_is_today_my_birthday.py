# test_is_today_my_birthday.py

from unittest.mock import patch
# from mock import patch

from about_time import is_today_my_birthday


@patch("about_time.get_today_info")
def test_is_birthday(mock_get_today_info):
    mock_get_today_info.return_value = (1, 20)
    assert is_today_my_birthday("01-20")


@patch("about_time.get_today_info")
def test_is_not_birthday(mock_get_today_info):
    mock_get_today_info.return_value = (10, 20)
    assert not is_today_my_birthday("01-20")