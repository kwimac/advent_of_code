def _find_start(data: list[list[str]]) -> tuple[int, int]:
    n, m = len(data), len(data[0])
    for y in range(m):
        for x in range(n):
            if data[y][x] == "^":
                return x, y

def task_1(data: list[list[str]]) -> int:
    data = [list(_line.strip()) for _line in data]
    n, m = len(data), len(data[0])
    steps = [(0,-1), (1,0), (0,1), (-1,0)]

    x,y = _find_start(data)
    ii = 0
    step = steps[ii]
    visited = set()
    while True:
        visited.add((x, y))
        xx, yy = x+step[0], y+step[1]
        if not(0<=yy<n and 0<=xx<m):
            return len(visited)
        if data[yy][xx] == "#":
            ii = (ii+1)%4
            step = steps[ii]
            continue
        x = xx
        y = yy



def task_2(data: list[str]) -> int:
    data = [list(_line.strip()) for _line in data]
    n, m = len(data), len(data[0])
    steps = [(0,-1), (1,0), (0,1), (-1,0)]

    def _creates_loop(x: int, y: int, ii: int) -> bool:
        visited = set()
        step = steps[ii]
        while True:
            if (x, y, ii) in visited:
                return True
            visited.add((x, y, ii))
            xx, yy = x+step[0], y+step[1]
            if not(0<=yy<n and 0<=xx<m):
                return False
            if data[yy][xx] == "#":
                ii = (ii+1)%4
                step = steps[ii]
                continue
            x = xx
            y = yy

    ii = 0
    step = steps[ii]
    positions = set()
    x, y= start = _find_start(data)
    while True:
        xx, yy = x+step[0], y+step[1]
        if not(0<=yy<n and 0<=xx<m):
            return len(positions)
        if data[yy][xx] == "#":
            ii = (ii+1)%4
            step = steps[ii]
            continue
        if data[yy][xx] !="^" and (xx,yy) not in positions:
            data[yy][xx] = "#"
            if _creates_loop(*start, 0):
                positions.add((xx, yy))
            data[yy][xx] = "."
        x = xx
        y = yy


if __name__ == "__main__":
    # with open("2024/data/example_06.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_06.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
    print(task_1(data_))
    print(task_2(data_))
