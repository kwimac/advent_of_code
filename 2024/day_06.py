from collections import defaultdict

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
    ii = 0
    step = steps[ii]
    counter = 1
    x,y = _find_start(data)
    data[y][x] = "X"
    x += step[0]
    y += step[1]
    while 0<=y<n and 0<=x<m:
        if data[y][x] == "#":
            x -= step[0]
            y -= step[1]
            ii = (ii+1)%4
            step = steps[ii]
        elif data[y][x] == ".":
            data[y][x] = "X"
            counter += 1
        x += step[0]
        y += step[1]
    return counter



def task_2(data: list[str]) -> int:
    data = [list(_line.strip()) for _line in data]
    n, m = len(data), len(data[0])
    steps = [(0,-1), (1,0), (0,1), (-1,0)]

    def _creates_loop(s_x: int, s_y: int, s_ii: int) -> bool:
        bounce_cache = defaultdict(set)
        s_step = steps[s_ii]
        while 0<=s_y<n and 0<=s_x<m:
            if data[s_y][s_x] == "#":
                if (
                    (bounces:=bounce_cache.get((s_x, s_y)))
                    and s_ii in bounces
                ):
                    return True
                bounce_cache[(s_x, s_y)].add(s_ii)
                s_x -= s_step[0]
                s_y -= s_step[1]
                s_ii = (s_ii+1)%4
                s_step = steps[s_ii]
            s_x += s_step[0]
            s_y += s_step[1]
        return False

    ii = 0
    step = steps[ii]
    postions = set()
    x,y = _find_start(data)
    while True:
        xx, yy = x+step[0], y+step[1]
        if not(0<=yy<n and 0<=xx<m):
            return len(postions)
        if data[yy][xx] == "#":
            ii = (ii+1)%4
            step = steps[ii]
            continue
        data[yy][xx] = "#"
        if _creates_loop(x, y, ii):
            postions.add((xx, yy))
        data[yy][xx] = "."
        x = xx
        y = yy


if __name__ == "__main__":
    with open("2024/data/example_06.txt", "r", encoding="utf-8") as _file:
    # with open("2024/data/input_06.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
    # print(task_1(data_))
    print(task_2(data_))
