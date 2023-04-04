__author__ = "730569503"


def short_words(input_list: list[str]) -> list[str]:
    output_list: list[str] = []
    for elem in input_list:
        if len(elem) >= 5:
            print(f"{elem} is too long!")
        elif len(elem) < 5:
            output_list.append(elem)
    return output_list