from collections import deque
from itertools import chain, repeat, takewhile
import pprint


ROBOT_SYMBOL = "@"
WALL_SYMBOL = "#"
BOX_SYMBOL = "O"
BOX_LEFT_SYMBOL = "["
BOX_RIGHT_SYMBOL = "]"
EMPTY_SYMBOL = "."
DIRECTIONS_MAP = {
    ">": (1,0), 
    "^": (0,-1),
    "<": (-1,0), 
    "v": (0,1), 
}


def _find_robot(board: list[list[str]]) -> tuple[int, int]:
    n, m = len(board), len(board[0])
    for y in range(n):
        for x in range(m):
            if board[y][x] == ROBOT_SYMBOL:
                return x, y
    

def task_1(data: list[str]) -> int:
    data = iter(data)
    board = [list(row.strip()) for row in takewhile(lambda x: x != "\n", data)]
    robot = _find_robot(board)
    for move in chain.from_iterable(row.strip() for row in data):
        _move_simple(board, robot, move)
        
    return _sum_gps(board)

def _move_simple(board: list[list[str]], robot: tuple[int, int], move: str) -> None:
    dx, dy = DIRECTIONS_MAP[move]
    px, py = robot
    x, y = px+dx, py+dy
    updates = deque([])
    while board[y][x] != WALL_SYMBOL:
        if board[y][x] == EMPTY_SYMBOL:
            while updates:
                board[y][x] = board[py][px]
                x, y = px, py
                px, py = updates.pop()
            board[y][x] = board[py][px]
            board[py][px] = "."
            robot = (x,y)
            break
        updates.append((px,py))
        px, py = x, y
        x, y = px+dx, py+dy


def _sum_gps(board: list[list[str]]) -> int:
    n, m = len(board), len(board[0])
    return sum(
        100*y+x
        for y in range(n)
        for x in range(m)
        if board[y][x] == BOX_SYMBOL
    )


def task_2(data: list[str]) -> int:
    data = iter(data)
    board = [
        list(
            chain.from_iterable(
                repeat(elem, 2) if elem != BOX_SYMBOL else [BOX_LEFT_SYMBOL, BOX_RIGHT_SYMBOL]
                for elem in row.strip()
            )
        )
        for row in takewhile(lambda x: x != "\n", data)
    ]
    robot = _find_robot(board)
    board[robot[1]][robot[0]+1] = "."
    for move in chain.from_iterable(row.strip() for row in data):
        if move in "v^":
            ...
        else:
            _move_simple(board, robot, move)
        print(move)
        pprint.pprint(board)
        
    return _sum_gps_2(board)

def _move_simple(board: list[list[str]], robot: tuple[int, int], move: str) -> None:
    dx, dy = DIRECTIONS_MAP[move]
    px, py = robot
    x, y = px+dx, py+dy
    updates = deque([])
    while board[y][x] != WALL_SYMBOL:
        if board[y][x] == EMPTY_SYMBOL:
            while updates:
                board[y][x] = board[py][px]
                    if board[y][x] == BOX_LEFT_SYMBOL:
                        board[y][x+1] = board[py][px+1]
                    elif board[y][x] == BOX_RIGHT_SYMBOL:
                        board[y][x-1] = board[py][px-1]
                x, y = px, py
                px, py = updates.pop()
            board[y][x] = board[py][px]
            board[py][px] = "."
            robot = (x,y)
            break
        updates.append((px,py))
        px, py = x, y
        x, y = px+dx, py+dy


def _get_to_check(board: list[list[str]],point: tuple[int, int], ppoint: tuple[int, int]) -> list[tuple[int, int]]:
    x, y, px, py = point, ppoint
    if 



def _sum_gps_2(board: list[list[str]]) -> int:
    n, m = len(board), len(board[0])
    return sum(
        100*y+x
        for y in range(n)
        for x in range(m)
        if board[y][x] == BOX_LEFT_SYMBOL
    )


if __name__ == "__main__":
    with open("2024/data/example_15.txt", "r", encoding="utf-8") as _file:
    # with open("2024/data/input_15.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        # print(task_1(data_))
        print(task_2(data_))
