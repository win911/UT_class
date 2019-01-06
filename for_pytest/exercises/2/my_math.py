# my_math.py

def is_multiples_of_three(num):
    if num % 3 == 0:
        return True
    else:
        return False


def insert_number(my_list, number_list):
    for num in number_list:
        if is_multiples_of_three(num):
            my_list.append(num)