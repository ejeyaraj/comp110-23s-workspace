"""EX-08 -  Data Wrangling."""

__author__ = "730569503"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close
    return result


def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    #step through table
    for row in table:
        # save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str,str]]) -> dict[str,list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys."""
    result: dict[str,list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str,str] = table[0]
    for key in first_row: 
        # for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result


def head(table: dict[str,list[str]], rows_int: int) -> dict[str,list[str]]:
    """When given a table and a number of rows, this function will return a new column-based table with only the specified number of rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in table:
        list_empty: list = []
        int_var: int = 0
        for item in table[column]:
            if rows_int > int_var:
                list_empty.append(item)
                int_var += 1
        result[column] = list_empty
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """When given a table and a list of names for columns, this function will return a new table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for name in names:
        result[name] = table[name]
    return result 


def concat(table: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """When given two tables, this function returns a new table with the two tables combined."""
    result: dict[str, list[str]] = {}
    for column in table:
        result[column] = table[column]
    for column in table2:
        if column in result:
            result[column] += table2[column]
        else:
            result[column] = table2[column]
    return result


def count(inp_list: list[str]) -> dict[str, int]:
    """Given a list, this function will produce a dict where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for item in inp_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result