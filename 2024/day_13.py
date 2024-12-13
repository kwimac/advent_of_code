from itertools import takewhile
import re
from typing import Generator


def _parse_input(data: list[str]) -> Generator[list[int], None, None]:
    data = iter(data)
    pattern = r".*: X[+=](\d+), Y[+=](\d+)"
    
    rows = list(takewhile(lambda x: x != "\n", data))
    while rows:
        yield [
            list(map(int, re.match(pattern, row.strip()).groups()))
            for row in rows
        ]
        rows = list(takewhile(lambda x: x != "\n", data))


def _solve_game(A: list[int], B: list[int], prize: list[int]) -> int:
    ax, ay = A
    bx, by = B
    px, py = prize

    b = (px*ay-ax*py)/(bx*ay-ax*by)
    if b % 1 == 0:
        b = int(b)
        a = (py-by*b)//ay
        return  3*a+b if a<100 and b<100 else 0
    else:
        return 0


def task_1(data: list[str]) -> int:
    games = _parse_input(data)
    return sum(_solve_game(*game) for game in games)


def _solve_game_2(A: list[int], B: list[int], prize: list[int]) -> int:
    ax, ay = A
    bx, by = B
    px, py = prize
    px += int(1e13)
    py += int(1e13)

    b = (px*ay-ax*py)/(bx*ay-ax*by)
    if b % 1 == 0:
        b = int(b)
        a = (py-by*b)//ay

        if ax/bx%1 ==0 or bx/ax%1==0:
            if ay/by%1 ==0 or by/ay%1==0:
                print(px, py, ax,ay, bx, by, (py-by*(px/bx))/ay)
        return  3*a+b
    else:
        return 0

def task_2(data: list[str]) -> int:
    games = _parse_input(data)
    return sum(_solve_game_2(*game) for game in games)


if __name__ == "__main__":
    # with open("2024/data/example_13.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_13.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        # print(task_1(data_))
        print(task_2(data_))
