# test_my_math.py

from my_math import insert_number


def test_insert_number():
    # === Case 1 ===
    my_list = []
    number_list = []
    insert_number(my_list, number_list)
    assert my_list == []

    # === Case 2 ===
    my_list = []
    number_list = [1, 2, 4, 5]
    insert_number(my_list, number_list)
    assert my_list == []

    # === Case 3 ===
    my_list = []
    number_list = [i for i in range(1, 11)]
    insert_number(my_list, number_list)
    assert my_list == [3, 6, 9]

    # === Case 4 ===
    my_list = [3, 12]
    number_list = []
    insert_number(my_list, number_list)
    assert my_list == [3, 12]

    # === Case 5 ===
    my_list = [3, 12]
    number_list = [5, 4, 2, 1]
    insert_number(my_list, number_list)
    assert my_list == [3, 12]

    # === Case 6 ===
    my_list = [3, 12]
    number_list = [91, 51, 32, 60, 24, 23, 11]
    insert_number(my_list, number_list)
    assert my_list == [3, 12, 51, 60, 24]