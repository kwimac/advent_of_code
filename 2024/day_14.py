from collections import defaultdict
from functools import reduce
from operator import mul
import re


Point = tuple[int, int]

def _parse_row(row: str) -> tuple[Point, Point]:
    pattern = r"p=(\d+,\d+) v=(-?\d+,-?\d+)"
    p, v = re.match(pattern, row.strip()).groups()
    p = tuple(map(int, p.split(",")))
    v = tuple(map(int, v.split(",")))
    return p,v

def task_1(data: list[str]) -> int:
    # n, m = 7, 11  # example
    n, m = 103, 101  # input
    n2, m2 = n//2, m//2
    seconds = 100

    quadrants = [0,0,0,0]
    for row in data:
        p, v = _parse_row(row)
        px = (p[0] + seconds*v[0]) % m
        py = (p[1] + seconds*v[1]) % n
        if px == m2 or py == n2:
            continue
        quadrants[2*int(px<m2)+int(py<n2)] += 1
    return reduce(mul, quadrants)

def has_border(points_map: dict[int, list[int]], border_len: int) -> bool:
    for row in points_map.values():
        sequence_len = 0
        row = sorted(row)
        for e1, e2 in zip(row[:-1], row[1:]):
            if e2-e1 == 1:
                sequence_len += 1
            else:
                if sequence_len ==border_len:
                    return True
                sequence_len = 0
    return False

def draw_board(m: int, n: int, points_map: dict[int, set[int]]) -> None:
    board = [["." for _ in range(m)] for _ in range(n)]
    for y, xs in points_map.items():
        for x in xs:
            board[y][x] = "#"
    print("\n".join("".join(row) for row in board))
    

def task_2(data: list[str]) -> int:
    n, m = 103, 101  # input

    s = 0
    while True:
        points_map = defaultdict(set)
        for row in data:
            p, v = _parse_row(row)
            px = (p[0] + s*v[0]) % m
            py = (p[1] + s*v[1]) % n
            points_map[py].add(px)
        if has_border(points_map, 8):
            draw_board(m, n, points_map)
            return s
        s += 1


if __name__ == "__main__":
    # with open("2024/data/example_14.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_14.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        # print(task_1(data_))
        print(task_2(data_))
