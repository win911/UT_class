# my_math.py

def is_multiples_of_three(num):
    if not isinstance(num, int):
        raise ValueError("The parameter MUST be an integer.")
    
    if num % 3 == 0:
        return True
    else:
        return False