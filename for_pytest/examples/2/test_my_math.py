# test_my_math.py

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