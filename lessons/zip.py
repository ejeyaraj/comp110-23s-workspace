def zip(str_list: list[str], int_list: list[int]) -> dict[str,int]:
    output_dict: dict = {}
    if len(str_list) != len(int_list) or str_list == [] or int_list == []:
        return output_dict
    
    for elem in range(len(str_list)):
        output_dict[str_list[elem]] = int_list[elem]

    return output_dict