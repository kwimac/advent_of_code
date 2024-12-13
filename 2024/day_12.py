from collections import deque
from re import A


DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]


def task_1(data: list[str]) -> int:
    data = [list(row.strip()) for row in data]
    n, m = len(data), len(data[0])

    def _get_fence_price(x, y) -> int:
        char = data[y][x]
        data[y][x] = '.'
        to_check = deque([(x,y)])
        visited = {(x,y)}
        area = 1
        sides = 4
        while to_check:
            x, y = to_check.popleft()
            for xx, yy in DIRECTIONS:
                xx += x
                yy += y
                if 0<=xx<m and 0<=yy<n:
                    if data[yy][xx] == char:
                        area += 1
                        sides += 3
                        data[yy][xx] = '.'
                        to_check.append((xx, yy))
                        visited.add((xx, yy))
                    elif (xx, yy) in visited:
                        sides -= 1
        return sides * area

    result = 0
    for y in range(n):
        for x in range(m):
            if data[y][x] != '.':
                result += _get_fence_price(x, y)
    return result
                

def task_2(data: list[str]) -> int:
    data = [list(row.strip()) for row in data]
    n, m = len(data), len(data[0])

    def _get_fence_price(x, y) -> int:
        char = data[y][x]
        to_check = deque([(x,y)])
        visited = {}
        area = 0
        sides = 0
        while to_check:
            x, y = to_check.popleft()
            if data[y][x] == '.':
                continue
            area += 1
            data[y][x] = '.'
            borders = set()
            for ii, (xx, yy) in enumerate(DIRECTIONS):
                xx += x
                yy += y
                if not(0<=xx<m and 0<=yy<n):
                    borders.add(ii)
                elif not(data[yy][xx] == char or (xx, yy) in visited):
                    borders.add(ii)
            sides += len(borders)
            visited[(x,y)] = borders
            for xx, yy in DIRECTIONS:
                xx += x
                yy += y
                if 0<=xx<m and 0<=yy<n:
                    if data[yy][xx] == char:
                        to_check.append((xx, yy))
                    elif (prev_borders := visited.get((xx, yy))):
                        sides -= len(borders.intersection(prev_borders))
        return sides * area

    result = 0
    for y in range(n):
        for x in range(m):
            if data[y][x] != '.':
                result += _get_fence_price(x, y)
    return result


if __name__ == "__main__":
    # with open("2024/data/example_12.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_12.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        # print(task_1(data_))
        print(task_2(data_))
