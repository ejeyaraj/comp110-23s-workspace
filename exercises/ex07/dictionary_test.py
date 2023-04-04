"""EX07 - Dictionary testing."""

__author__ = "730569503"

import pytest
from dictionary import invert, favorite_color, count


def test_empty_dict() -> None:
    """Given an empty dict, this function will return an empty dict when calling the function invert."""
    assert invert({}) == {}


def test_many() -> None:
    """Given a dict with many strings, this function will invert the dictionary and return a dictionary with inverted values when calling the funtion invert."""
    test_dict: dict[str, str] = {"left": "right", "yin": "yang", "up": "down"}
    output_dict: dict[str, str] = {"right": "left", "yang": "yin", "down": "up"}
    assert invert(test_dict) == output_dict


with pytest.raises(KeyError):
    """Given a dict with values that are the same, this function will raise a KeyError when calling the function invert."""
    test_dict: dict[str, str] = {"green": "white", "black": "white"}
    invert(test_dict)


def test_empty_colors() -> None:
    """Given an empty dict, this function will return None when calling the function favorite_color."""
    assert favorite_color({}) == ""


def test_many_colors() -> None:
    """Given a dict with many strings, this function will return the string value that appears most often when calling the function favorite_color."""
    test_dict: dict[str, str] = {"Katniss": "green", "Gale": "white", "Peeta": "green"}
    assert favorite_color(test_dict) == "green"


def test_many_colors_tie() -> None:
    """Given a dict with many strings and a tie for the string value that appears most often, this function will return the string value that appeared first in the input dictionary in order to break the tie when calling the function favorite_color."""
    test_dict: dict[str, str] = {"Katniss": "green", "Gale": "white", "Peeta": "green", "Primrose": "white"}
    assert favorite_color(test_dict) == "green"


def test_empty_list() -> None:
    """Given an empty list, this function will return an empty dict when calling the function count."""
    assert count([]) == {}


def test_many_list() -> None:
    """Given a list, this function will produce a dict where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list when calling the function count."""
    test_list: list[str] = ["netflix", "netflix", "spotify", "amazon", "instagram", "spotify"]
    assert count(test_list) == {"netflix": 2, "spotify": 2, "amazon": 1, "instagram": 1}


def test_one() -> None:
    """Given a list with only one item, this function will produce a dict with the item as the key and the integer 1 as the value when calling the function count."""
    test_list: list[str] = ["apple"]
    assert count(test_list) == {"apple": 1}