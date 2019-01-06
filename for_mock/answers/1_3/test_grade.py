# test_grade.py

from unittest.mock import patch
# from mock import patch

from student import grade


@patch("student.utils.get_scores_from_db")
def test_grade_A(mock_get_scores):
    mock_get_scores.return_value = [80, 90, 100]

    result = grade("Maomao")

    assert result == "A"


@patch("student.utils.get_scores_from_db")
def test_grade_B(mock_get_scores):
    mock_get_scores.return_value = [60, 70, 75]

    result = grade("Maomao")

    assert result == "B"


@patch("student.utils.get_scores_from_db")
def test_grade_C(mock_get_scores):
    mock_get_scores.return_value = [40, 50, 60]

    result = grade("Maomao")

    assert result == "C"