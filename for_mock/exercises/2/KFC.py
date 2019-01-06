# KFC.py

from random import randint, choice


def give_fried_chicken(number):
    pass


def give_french_fries(number):
    pass


def give_custard_tarts(number):
    pass


def get_user_order():
    return randint(1, 10), choice(["Fried chicken", "French fries", "Custard Tarts"])


def process_user_order():
    number, item = get_user_order()
    if item == "Fried chicken": # buy five, get one free
        number += number // 5
        give_fried_chicken(number)
    elif item == "French fries":
        give_french_fries(number)
    elif item == "Custard Tarts": # buy three, get one free
        number += number // 3
        give_custard_tarts(number)