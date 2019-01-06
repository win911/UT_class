# my_math.py

def fibonacci(num):
    if num == 0 or num == 1:
        return 1
    else:
        return fibonacci(num-2) + fibonacci(num-1)