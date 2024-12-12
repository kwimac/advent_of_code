from collections import deque


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
            for xx, yy in [(1,0), (0,1), (-1,0), (0,-1)]:
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
        data[y][x] = '.'
        to_check = deque([(x,y)])
        visited = {(x,y)}
        area = 1
        sides = 4
        while to_check:
            x, y = to_check.popleft()
            for xx, yy in [(1,0), (0,1), (-1,0), (0,-1)]:
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


if __name__ == "__main__":
    # with open("2024/data/example_12.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_12.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        print(task_1(data_))
        # print(task_2(data_))
