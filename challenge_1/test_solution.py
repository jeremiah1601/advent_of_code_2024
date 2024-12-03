import pytest
from solution import solution

def test_solution_basic_1():
    list_1 = [3,4, 2, 1, 3, 3]
    list_2 = [4, 3, 5, 3, 9, 3]
    assert solution(list_1, list_2) == 11