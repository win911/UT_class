# test_display_user_info.py

from unittest.mock import patch, MagicMock
# from mock import patch, MagicMock

from account import display_user_info


@patch("account.get_user")
def test_adult(mock_user):
    fake_user = MagicMock()
    fake_user.username = "Maomao"
    fake_user.is_adult.return_value = True
    mock_user.return_value = fake_user

    html = display_user_info(100)

    assert html == "<h1>Maomao (Adult)</h1>"


@patch("account.get_user")
def test_child(mock_user):
    fake_user = MagicMock()
    fake_user.username = "Maomao"
    fake_user.is_adult.return_value = False
    mock_user.return_value = fake_user

    html = display_user_info(100)

    assert html == "<h1>Maomao (Child)</h1>"