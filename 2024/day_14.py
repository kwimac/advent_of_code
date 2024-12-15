from functools import reduce
from operator import mul
import re
import time


def task_1(data: list[str]) -> int:
    # n, m = 7, 11  # example
    n, m = 103, 101  # input
    n2, m2 = n//2, m//2
    seconds = 100

    pattern = r"p=(\d+,\d+) v=(-?\d+,-?\d+)"
    quadrants = [0,0,0,0]
    for row in data:
        p, v = re.match(pattern, row.strip()).groups()
        p = tuple(map(int, p.split(",")))
        v = tuple(map(int, v.split(",")))
        px = (p[0] + seconds*v[0]) % m
        py = (p[1] + seconds*v[1]) % n
        if px == m2 or py == n2:
            continue
        quadrants[2*int(px<m2)+int(py<n2)] += 1
    return reduce(mul, quadrants)

def task_2(data: list[str]) -> int:
    n, m = 103, 101  # input
    goback = "\033[F" * n

    pattern = r"p=(\d+,\d+) v=(-?\d+,-?\d+)"
    for row in data:
        p, v = re.match(pattern, row.strip()).groups()
        p = tuple(map(int, p.split(",")))
        v = tuple(map(int, v.split(",")))
    for s in range(10):
        output = [[0 for _ in range(m)] for _ in range(n)]
        px = (p[0] + s*v[0]) % m
        py = (p[1] + s*v[1]) % n
        output[py][px] += 1
        print(
            f"{goback}{s}\n"
            "\n".join("".join(map(str, row)) for row in output)
        )
        time.sleep(1)


if __name__ == "__main__":
    # with open("2024/data/example_14.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_14.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        # print(task_1(data_))
        print(task_2(data_))
