# utils.py

from random import randint


def get_scores_from_db(name):
    return [randint(1, 100) for i in range(3)]