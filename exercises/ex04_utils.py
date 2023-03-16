"""EX04 - `list` Utility Functions - Implementing algorithms and writing functions."""

__author__: str = "730569503"


def all(num_list: list[int], num: int) -> bool:
    """Given a list of integers and a number, this function returns whether or not all the integers in the list are the same as the number."""
    if len(num_list) == 0:
        print("False")
        return False

    check_indice: int = 0
    while check_indice < len(num_list) - 1:
        if num_list[check_indice] == num:
            check_indice += 1
        else:
            print("False")
            return False

    print("True")        
    return True


def max(num_list: list[int]) -> int:
    """Given a list of integers, return the largest integer."""
    if len(num_list) == 0:
        raise ValueError("max() is an empty List")
    
    check_indice: int = 0
    max_int: int = num_list[check_indice]
    while check_indice < len(num_list) - 1:
        if num_list[check_indice] < num_list[check_indice + 1] and max_int < num_list[check_indice + 1]:
            max_int = num_list[check_indice + 1]
            check_indice += 1
        else:
            if num_list[check_indice] > max_int: 
                max_int = num_list[check_indice]
                check_indice += 1
            else:
                check_indice += 1

    print(max_int)
    return max_int


def is_equal(num_list_one: list[int], num_list_two: list[int]) -> bool:
    """Given two lists of integers, return True if every element at every index is equal in both lists."""
    if len(num_list_one) != len(num_list_two):
        print("False")
        return False

    check_indice: int = 0
    while check_indice < len(num_list_one) - 1:
        if num_list_one[check_indice] == num_list_two[check_indice]:
            check_indice += 1
        else:
            print("False")
            return False

    print("True")
    return True