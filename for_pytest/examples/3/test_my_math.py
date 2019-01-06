# test_my_math.py

from pytest import raises

from my_math import fibonacci


class Testfibonacci(object):
    def test_value(self):
        assert fibonacci(0) == 1
        assert fibonacci(1) == 1
        assert fibonacci(2) == 2
        assert fibonacci(3) == 3
        assert fibonacci(4) == 5
        assert fibonacci(5) == 8
        
    def test_cache(self):
        def _verify_result(num, cache):
            for i in range(num+1):
                assert i in cache
            assert num+1 not in cache

        # === Case 1 ===
        cache = {
            0: 1,
            1: 1
        }
        fibonacci(3, cache=cache)
        _verify_result(3, cache)

        # === Case 2 ===
        cache = {}
        fibonacci(5, cache=cache)
        _verify_result(5, cache)

    def test_invalid_parameter(self):
        with raises(ValueError) as e:
            fibonacci("123")
        assert str(e.value) == "Usage: fibonacci(num=<int>, cahce=<dict>)"

        with raises(ValueError) as e:
            fibonacci(123, cache=[])
        assert str(e.value) == "Usage: fibonacci(num=<int>, cahce=<dict>)"