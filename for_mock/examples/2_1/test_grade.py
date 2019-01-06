# test_grade.py

from unittest.mock import patch
# from mock import patch

from student import grade


@patch("student.get_scores_from_db")
def test_success_case(mock_get_scores):
    mock_get_scores.return_value = [80, 90, 100]

    grade("Maomao")

    mock_get_scores.assert_called_once()
    # assert mock_get_scores.call_count == 1


@patch("student.get_scores_from_db")
def test_failed_case(mock_get_scores):
    mock_get_scores.return_value = [80, 90, 100]

    grade("Maomao")
    grade("Abby")

    mock_get_scores.assert_called_once()
    # assert mock_get_scores.call_count == 1