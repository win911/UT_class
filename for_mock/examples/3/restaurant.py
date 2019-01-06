# restaurant.py

def is_today_birthday():
    pass


def prepare_a_cake():
    pass


def print_error(error):
    pass


def celebrate_for_customer(customer_birthday):
    try:
        if is_today_birthday(customer_birthday):
            prepare_a_cake()
    except ValueError as e:
        print_error(e)