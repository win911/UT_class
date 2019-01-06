# test_celebrate_for_customer.py

from unittest.mock import patch
# from mock import patch

from restaurant import celebrate_for_customer


@patch("restaurant.print_error")
@patch("restaurant.is_today_birthday")
def test_invalid_input(mock_is_today_birthday, mock_print_error):
    mock_is_today_birthday.side_effect = ValueError("Invalid input")
    # Otherwise, you can write like this (more powerful)
    # def fake_is_today_birthday(birthday):
    #    raise ValueError("Invalid input")
    # mock_is_today_birthday.side_effect = fake_is_today_birthday

    celebrate_for_customer("01-01")

    mock_print_error.assert_called_once() # assert mock_print_error.call_count == 1