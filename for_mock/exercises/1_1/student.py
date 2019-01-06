# student.py

from random import randint


def get_scores_from_db(name):
    return [randint(1, 100) for i in range(3)]


def grade(name):
    scores = get_scores_from_db(name)
    total_score = sum(scores)
    quotient = total_score // len(scores)

    if quotient >= 80:
        return "A"
    elif quotient >= 60:
        return "B"
    else:
        return "C"