# test_process_user_order.py

from unittest.mock import patch
# from mock import patch

from KFC import process_user_order


@patch("KFC.give_custard_tarts")
@patch("KFC.give_french_fries")
@patch("KFC.give_fried_chicken")
@patch("KFC.get_user_order")
def test_order_two_fried_chicken(mock_get_user_order, mock_give_fried_chicken, mock_give_french_fries,
                                 mock_give_custard_tarts): 
    mock_get_user_order.return_value = (2, "Fried chicken")

    process_user_order()

    mock_get_user_order.assert_called_once() # assert mock_get_user_order.call_count == 1
    mock_give_fried_chicken.assert_called_once_with(2)
    mock_give_french_fries.assert_not_called()
    mock_give_custard_tarts.assert_not_called()


@patch("KFC.give_custard_tarts")
@patch("KFC.give_french_fries")
@patch("KFC.give_fried_chicken")
@patch("KFC.get_user_order")
def test_order_seven_fried_chicken(mock_get_user_order, mock_give_fried_chicken, mock_give_french_fries,
                                   mock_give_custard_tarts):
    mock_get_user_order.return_value = (7, "Fried chicken")

    process_user_order()

    mock_get_user_order.assert_called_once() # assert mock_get_user_order.call_count == 1
    mock_give_fried_chicken.assert_called_once_with(8)
    mock_give_french_fries.assert_not_called()
    mock_give_custard_tarts.assert_not_called()


@patch("KFC.give_custard_tarts")
@patch("KFC.give_french_fries")
@patch("KFC.give_fried_chicken")
@patch("KFC.get_user_order")
def test_order_ten_fried_chicken(mock_get_user_order, mock_give_fried_chicken, mock_give_french_fries,
                                 mock_give_custard_tarts):
    mock_get_user_order.return_value = (10, "Fried chicken")

    process_user_order()

    mock_get_user_order.assert_called_once() # assert mock_get_user_order.call_count == 1
    mock_give_fried_chicken.assert_called_once_with(12)
    mock_give_french_fries.assert_not_called()
    mock_give_custard_tarts.assert_not_called()


@patch("KFC.give_custard_tarts")
@patch("KFC.give_french_fries")
@patch("KFC.give_fried_chicken")
@patch("KFC.get_user_order")
def test_order_two_french_fries(mock_get_user_order, mock_give_fried_chicken, mock_give_french_fries,
                                mock_give_custard_tarts):
    mock_get_user_order.return_value = (2, "French fries")

    process_user_order()

    mock_get_user_order.assert_called_once() # assert mock_get_user_order.call_count == 1
    mock_give_fried_chicken.assert_not_called()
    mock_give_french_fries.assert_called_once_with(2)
    mock_give_custard_tarts.assert_not_called()


@patch("KFC.give_custard_tarts")
@patch("KFC.give_french_fries")
@patch("KFC.give_fried_chicken")
@patch("KFC.get_user_order")
def test_order_seven_french_fries(mock_get_user_order, mock_give_fried_chicken, mock_give_french_fries,
                                  mock_give_custard_tarts):
    mock_get_user_order.return_value = (7, "French fries")

    process_user_order()

    mock_get_user_order.assert_called_once() # assert mock_get_user_order.call_count == 1
    mock_give_fried_chicken.assert_not_called()
    mock_give_french_fries.assert_called_once_with(7)
    mock_give_custard_tarts.assert_not_called()


@patch("KFC.give_custard_tarts")
@patch("KFC.give_french_fries")
@patch("KFC.give_fried_chicken")
@patch("KFC.get_user_order")
def test_order_ten_french_fries(mock_get_user_order, mock_give_fried_chicken, mock_give_french_fries,
                                mock_give_custard_tarts):
    mock_get_user_order.return_value = (10, "French fries")

    process_user_order()

    mock_get_user_order.assert_called_once() # assert mock_get_user_order.call_count == 1
    mock_give_fried_chicken.assert_not_called()
    mock_give_french_fries.assert_called_once_with(10)
    mock_give_custard_tarts.assert_not_called()


@patch("KFC.give_custard_tarts")
@patch("KFC.give_french_fries")
@patch("KFC.give_fried_chicken")
@patch("KFC.get_user_order")
def test_order_two_custard_tarts(mock_get_user_order, mock_give_fried_chicken, mock_give_french_fries,
                                 mock_give_custard_tarts):
    mock_get_user_order.return_value = (2, "Custard Tarts")

    process_user_order()

    mock_get_user_order.assert_called_once() # assert mock_get_user_order.call_count == 1
    mock_give_fried_chicken.assert_not_called()
    mock_give_french_fries.assert_not_called()
    mock_give_custard_tarts.assert_called_once_with(2)


@patch("KFC.give_custard_tarts")
@patch("KFC.give_french_fries")
@patch("KFC.give_fried_chicken")
@patch("KFC.get_user_order")
def test_order_seven_custard_tarts(mock_get_user_order, mock_give_fried_chicken, mock_give_french_fries,
                                   mock_give_custard_tarts):
    mock_get_user_order.return_value = (7, "Custard Tarts")

    process_user_order()

    mock_get_user_order.assert_called_once() # assert mock_get_user_order.call_count == 1
    mock_give_fried_chicken.assert_not_called()
    mock_give_french_fries.assert_not_called()
    mock_give_custard_tarts.assert_called_once_with(9)


@patch("KFC.give_custard_tarts")
@patch("KFC.give_french_fries")
@patch("KFC.give_fried_chicken")
@patch("KFC.get_user_order")
def test_order_ten_custard_tarts(mock_get_user_order, mock_give_fried_chicken, mock_give_french_fries,
                                 mock_give_custard_tarts):
    mock_get_user_order.return_value = (10, "Custard Tarts")

    process_user_order()

    mock_get_user_order.assert_called_once() # assert mock_get_user_order.call_count == 1
    mock_give_fried_chicken.assert_not_called()
    mock_give_french_fries.assert_not_called()
    mock_give_custard_tarts.assert_called_once_with(13)