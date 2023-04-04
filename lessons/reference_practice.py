a: int = 3
b: int = 0
c: float

def main() -> None:
    global a
    global b
    print(fun(a,b))

def fun(a: int, b:int) -> list[int]:
    global c
    nums: list[int] = []
    if b == 0:
        while len(nums) < 4:
            c = a + b