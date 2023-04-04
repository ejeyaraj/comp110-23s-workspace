"""EX07- Practice with Dictionary Functions."""

__author__ = "730569503"


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, the function will invert the values and return a dictionary with the inverted values."""
    outp_dict: dict[str, str] = {}
    for key in inp_dict:
        value: str = inp_dict[key]
        if key in outp_dict or value in outp_dict:
            raise KeyError("Duplicate value found while inverting dictionary.")
        outp_dict[value] = key
    return outp_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Given an input dict, the function will return the color that appeared most often.""" 
    freq: dict[str, int] = {}
    max_freq: int = 0
    most_popular: list[str] = []
    color: str = ""
    for name in colors:
        color = colors[name]
        if color in freq:
            freq[color] += 1
        else:
            freq[color] = 1
        if freq[color] > max_freq:
            max_freq = freq[color]
            most_popular = [color]
        elif freq[color] == max_freq:
            most_popular.append(color)
    for name in colors:
        color = colors[name]
        if color in most_popular:
            return color
    return color
        

def count(inp_list: list[str]) -> dict[str, int]:
    """Given a list, this function will produce a dict where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for item in inp_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result