# KFC.py

def get_order():
    pass


def cook(order):
    pass


def close_door():
    pass


def notify_manager():
    pass


def front_desk():
    order = get_order()
    try:
        food = cook(order)
        return food
    except RuntimeError as e:
        if "Sold Out" in str(e):
            close_door()
        else:
            notify_manager()