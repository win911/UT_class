# student.py

import utils


def grade(name):
    scores = utils.get_scores_from_db(name)
    total_score = sum(scores)
    quotient = total_score // len(scores)

    if quotient >= 80:
        return "A"
    elif quotient >= 60:
        return "B"
    else:
        return "C"