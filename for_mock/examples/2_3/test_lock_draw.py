# test_lock_draw.py

from unittest.mock import patch
# from mock import patch

from party import lucky_draw


@patch("party.give_grape")
@patch("party.give_banana")
@patch("party.give_guava")
@patch("party.give_apple")
def test_get_red_ball(mock_give_apple, mock_give_guava, mock_give_banana, mock_give_grape):
    lucky_draw("Red")

    mock_give_apple.assert_called_once() # assert mock_give_apple.call_count == 1
    mock_give_guava.assert_not_called()
    mock_give_banana.assert_not_called()
    mock_give_grape.assert_not_called()