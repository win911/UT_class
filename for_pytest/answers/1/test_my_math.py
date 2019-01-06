# test_my_math.py

from my_math import is_multiples_of_three


def test_is_multiples_of_three():
    assert is_multiples_of_three(15)
    assert not is_multiples_of_three(23)
    assert is_multiples_of_three(42)
    assert is_multiples_of_three(51)
    assert not is_multiples_of_three(67)