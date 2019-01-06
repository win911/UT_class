# test_front_desk.py

from unittest.mock import patch
# from mock import patch

from KFC import front_desk


@patch("KFC.close_door")
@patch("KFC.cook")
def test_sold_out(mock_cook, mock_close_door):
    mock_cook.side_effect = RuntimeError("Sold Out!")

    front_desk()

    mock_close_door.assert_called_once() # assert mock_close_door.call_count == 1


@patch("KFC.notify_manager")
@patch("KFC.cook")
def test_other_runtime_error(mock_cook, mock_notify_manager):
    mock_cook.side_effect = RuntimeError("Refrigerator Broken!")

    front_desk()

    mock_notify_manager.assert_called_once() # assert mock_notify_manager.call_count == 1