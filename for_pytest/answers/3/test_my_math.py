# test_my_math.py

from pytest import raises

from my_math import is_multiples_of_three


def test_invalid_parameter_for_is_multiples_of_three():
    with raises(ValueError) as e:
        is_multiples_of_three("123")
    assert str(e.value) == "The parameter MUST be an integer."