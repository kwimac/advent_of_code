from collections import deque


def task_1(data: list[str]) -> int:
    data = [list(map(int, line.strip())) for line in data]
    n, m = len(data), len(data[0])

    def traverse(x: int, y: int) -> int:
        steps = deque([(x,y,1)])
        tops = set()
        while steps:
            x, y, v = steps.popleft()
            for sx, sy in [(1,0), (0,1), (-1,0), (0,-1)]:
                sx += x
                sy += y
                if 0<=sx<m and 0<=sy<n and data[sy][sx] == v:
                    if v == 9:
                        tops.add((sx, sy))
                    else:
                        steps.appendleft((sx,sy,v+1))
        return len(tops)

    return sum(
        traverse(x, y)
        for y in range(n)
        for x in range(m)
        if data[y][x] == 0
    )


def task_2(data: list[str]) -> int:
    data = [list(map(int, line.strip())) for line in data]
    n, m = len(data), len(data[0])

    def traverse(x: int, y: int) -> int:
        steps = deque([(x,y,1)])
        score = 0
        while steps:
            x, y, v = steps.popleft()
            for sx, sy in [(1,0), (0,1), (-1,0), (0,-1)]:
                sx += x
                sy += y
                if 0<=sx<m and 0<=sy<n and data[sy][sx] == v:
                    if v == 9:
                        score+=1
                    else:
                        steps.appendleft((sx,sy,v+1))
        return score

    return sum(
        traverse(x, y)
        for y in range(n)
        for x in range(m)
        if data[y][x] == 0
    )


if __name__ == "__main__":
    # with open("2024/data/example_010.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_010.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        # print(task_1(data_))
        print(task_2(data_))
