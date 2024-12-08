from collections import defaultdict
from itertools import chain


def task_1(data: list[str]) -> int:
    data = [line.strip() for line in data]
    n, m = len(data), len(data[0])
    antenas = defaultdict(list)
    nodes = set()
    for jj in range(n):
        for ii in range(m):
            if data[jj][ii] != ".":
                for y, x in antenas.get(data[jj][ii], []):
                    v_y, v_x = y-jj, x-ii
                    if 0<=v_y+y<n and 0<=v_x+x<m:
                        nodes.add((v_y+y, v_x+x))
                    if 0<=jj-v_y<n and 0<=ii-v_x<m:
                        nodes.add((jj-v_y, ii-v_x))
                antenas[data[jj][ii]].append((jj, ii))
    return len(nodes)


def task_2(data: list[str]) -> int:
    data = [line.strip() for line in data]
    n, m = len(data), len(data[0])
    antenas = defaultdict(list)
    nodes = set()
    for jj in range(n):
        for ii in range(m):
            if data[jj][ii] != ".":
                for y, x in antenas.get(data[jj][ii], []):
                    v_y, v_x = y-jj, x-ii
                    yn, xn = v_y+y, v_x+x
                    while 0<=yn<n and 0<=xn<m:
                        nodes.add((yn, xn))
                        yn += v_y
                        xn += v_x
                    yn, xn = jj-v_y, ii-v_x
                    while 0<=yn<n and 0<=xn<m:
                        nodes.add((yn, xn))
                        yn -= v_y
                        xn -= v_x
                antenas[data[jj][ii]].append((jj, ii))
    return len(nodes.union(chain.from_iterable(antenas.values())))


if __name__ == "__main__":
    # with open("2024/data/example_08.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_08.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        # print(task_1(data_))
        print(task_2(data_))
