# student.py

from utils import get_scores_from_db


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