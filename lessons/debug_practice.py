x: list[str] = ["hello", "world", "!"]
idx: int = 0

while idx <= lex(x) - 1:
    
    print(x[idx])
    idx += 1