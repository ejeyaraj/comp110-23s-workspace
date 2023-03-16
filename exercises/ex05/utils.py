"""EX05 Part 1 - `list` Utility Functions - Build list utility functions."""

__author__: str = "730569503"


def only_evens(int_list: list[int]) -> list:
    """Given a list of ints, the function will return a new list containing only the even integers of the input."""
    output_list: list[int] = []
    for num in int_list:
        if num % 2 == 0:
            output_list.append(num)
    print(output_list)
    return output_list


def concat(int_list_one: list[int], int_list_two: list[int]) -> list:
    """Given two lists of integers, this function will output a new list which has all the elements of the first list followed by the elements of the second list."""
    output_list: list[int] = []
    for num in int_list_one:
        output_list.append(num)
    
    for num in int_list_two:
        output_list.append(num)
    
    print(output_list)
    return output_list


def sub(int_list: list[int], start_idx: int, end_idx: int) -> list:
    """Given a list of integers, a start index, and a non-inclusive end index, this function will generate a subset of the input list with the specified start index and end index - 1."""
    output_list: list[int] = []

    if start_idx < 0:
        start_idx = 0

    if end_idx > len(int_list):
        end_idx = len(int_list) - 1
        while start_idx <= end_idx:
            output_list.append(int_list[start_idx])
            start_idx += 1

        print(output_list)
        return output_list

    if len(int_list) == 0 or start_idx >= len(int_list) or end_idx <= 0:
        print(output_list)
        return output_list

    while start_idx < end_idx:
        output_list.append(int_list[start_idx])
        start_idx += 1

    print(output_list)
    return output_list