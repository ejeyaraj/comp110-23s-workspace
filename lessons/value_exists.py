def value_exists(inp_dict: dict[str,int], val: int) -> bool:
    exists: bool = False
    for elem in inp_dict:
        if inp_dict[elem] == val:
            exists = True
    return exists
        