from collections import deque
from itertools import chain, repeat, takewhile
import pprint
from typing import Iterable


class Board:
    ROBOT_SYMBOL = "@"
    WALL_SYMBOL = "#"
    BOX_SYMBOL = "O"
    EMPTY_SYMBOL = "."
    DIRECTIONS_MAP = {
        ">": (1,0), 
        "^": (0,-1),
        "<": (-1,0), 
        "v": (0,1), 
    }

    def __init__(self, board: Iterable[str]) -> None:
        self.board = [list(row.strip()) for row in board]
        self.robot = self._find_robot()

    def _find_robot(self) -> tuple[int, int]:
        n, m = len(self.board), len(self.board[0])
        for y in range(n):
            for x in range(m):
                if self.board[y][x] == self.ROBOT_SYMBOL:
                    return x, y

    def sum_gps(self) -> int:
        n, m = len(self.board), len(self.board[0])
        return sum(
            100*y+x
            for y in range(n)
            for x in range(m)
            if self.board[y][x] == self.BOX_SYMBOL
        )

    def move_robot(self, move: str) -> None:
        dx, dy = self.DIRECTIONS_MAP[move]
        px, py = self.robot
        x, y = px+dx, py+dy
        updates = deque([])
        while self.board[y][x] != self.WALL_SYMBOL:
            if self.board[y][x] == self.EMPTY_SYMBOL:
                while updates:
                    self.board[y][x] = self.board[py][px]
                    x, y = px, py
                    px, py = updates.pop()
                self.board[y][x] = self.board[py][px]
                self.board[py][px] = "."
                self.robot = (x,y)
                break
            updates.append((px,py))
            px, py = x, y
            x, y = px+dx, py+dy
    

def task_1(data: list[str]) -> int:
    data = iter(data)
    board = Board(takewhile(lambda x: x != "\n", data))
    for move in chain.from_iterable(row.strip() for row in data):
        board.move_robot(move)
        
    return board.sum_gps()


class BroadBoard(Board):
    BOX_LEFT_SYMBOL = "["
    BOX_RIGHT_SYMBOL = "]"

    def __init__(self, board: Iterable[str]) -> None:
        self.board = board = [
            list(
                chain.from_iterable(
                    (
                        repeat(elem, 2) 
                        if elem != self.BOX_SYMBOL 
                        else [self.BOX_LEFT_SYMBOL, self.BOX_RIGHT_SYMBOL]
                    )
                    for elem in row.strip()
                )
            )
            for row in board
        ]
        self.robot = self._find_robot()
        self.board[self.robot[1]][self.robot[0]+1] = self.EMPTY_SYMBOL

    def sum_gps(self) -> int:
        n, m = len(self.board), len(self.board[0])
        return sum(
            100*y+x
            for y in range(n)
            for x in range(m)
            if self.board[y][x] == self.BOX_LEFT_SYMBOL
        )

    def move_robot(self, move: str) -> None:
        if move in "v^":
            ...
        else:
            super().move_robot(move)

    def _move_robot_vertically(self, move: str) -> Noe:


def _move_simple(board: list[list[str]], robot: tuple[int, int], move: str) -> None:
    dx, dy = self.DIRECTIONS_MAP[move]
    px, py = self.robot
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



def task_2(data: list[str]) -> int:
    data = iter(data)
    board = BroadBoard(takewhile(lambda x: x != "\n", data))
    for move in chain.from_iterable(row.strip() for row in data):
        board.move_robot(move)
        print(move)
        pprint.pprint(board)


if __name__ == "__main__":
    with open("2024/data/example_15.txt", "r", encoding="utf-8") as _file:
    # with open("2024/data/input_15.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        # print(task_1(data_))
        print(task_2(data_))
