"""EX05 Part 2 - `list` Utility Functions - Write unit tests."""

__author__: str = "730569503"

from utils import only_evens, sub, concat


def test_empty() -> None:
    """Given an empty list, this function will return an empty list when calling the function only_evens."""
    assert only_evens([]) == []


def test_many() -> None:
    """Given a list with many integers, this function will return only the even integers when calling the function only_evens."""
    test_list: list[int] = [100, 103, 106, 109, 112]
    output_test_list: list[int] = [100, 106, 112]
    while len(only_evens(test_list)) == 3:
        idx: int = 0
        if only_evens(test_list[idx]) == output_test_list[idx]:
            idx += 1


def test_many_with_negatives() -> None:
    """Given a list with many integers, including negative integers, this function will return the even integers when calling the function only_evens."""
    test_list: list[int] = [4, -4, -8, -11, -16, 3, 2]
    assert only_evens(test_list) == [4, -4, -8, -16, 2]


def test_empty_list() -> None:
    """Given an empty list, a start index, and end index, this function will return an empty list when calling the function sub."""
    assert sub([], 2, 3) == []


def test_many_in_list() -> None:
    """Given a list with many integers, a start index, and an end index, this function will return a subset of the input list with the specified start index and end index - 1 when calling the function sub."""
    test_list: list[int] = [10, 15, 20, 25, 30]
    assert sub((test_list), 2, 4) == [20, 25]


def test_incorrect_end_idx() -> None:
    """Given a list with many integers, a start index, and a end index that is greater than the length of the input list, this function will return a subset of the input list with the specified start index and an end index that is the length of the list - 1 when calling the fucntion sub."""
    test_list: list[int] = [10, 15, 20, 25, 30]
    assert sub((test_list), 3, 9) == [25,30]


def test_empty_lists() -> None:
    """Given two empty lists, this function will return an empty list when calling the function concat."""
    assert concat([], []) == []


def test_many_in_lists() -> None:
    """Given two lists with many integers, this function will return a list with the integers from the first list following the integers from the second list when calling the function concat."""
    test_list_one: list[int] = [4, 3, 2, 1]
    test_list_two: list[int] = [0, -1, -2, -3]
    assert concat(test_list_one, test_list_two) == [4, 3, 2, 1, 0, -1, -2, -3]


def test_emptyList_and_manyList() -> None:
    """Given one empty list and one list with many integers, this function will return a list with the integers from the second list when calling the function concat."""
    test_list_one: list[int] = []
    test_list_two: list[int] = [1, 2, 3]
    assert concat(test_list_one, test_list_two) == [1, 2, 3]