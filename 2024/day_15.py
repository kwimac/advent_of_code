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
            self._move_robot_vertically(move)
        else:
            super().move_robot(move)

    def _move_robot_vertically(self, move: str) -> None:
        dx, dy = self.DIRECTIONS_MAP[move]
        px, py = self.robot
        to_check = deque([(px, py, px+dx, py+dy)])
        updates = deque([])
        while to_check:
            px, py, x, y = to_check.popleft()
            if (px, py, x, y) in updates:
                continue
            char = self.board[y][x]
            updates.append((px,py, x, y))
            if char == self.WALL_SYMBOL:
                return
            if char == self.EMPTY_SYMBOL:
                continue
            if char != self.board[py][px]:
                if char == self.BOX_LEFT_SYMBOL:
                    to_check.append((x+1, y, x+dx+1, y+dy))
                elif char == self.BOX_RIGHT_SYMBOL:
                    to_check.append((x-1, y, x+dx-1, y+dy))
            to_check.append((x, y, x+dx, y+dy))
        while updates:
            px, py, x, y = updates.pop()
            tmp = self.board[y][x]
            self.board[y][x] = self.board[py][px]
            self.board[py][px] = tmp
        self.robot = (x,y)


def task_1(data: list[str]) -> int:
    data = iter(data)
    board = Board(takewhile(lambda x: x != "\n", data))
    for move in chain.from_iterable(row.strip() for row in data):
        board.move_robot(move)
        
    return board.sum_gps()


def task_2(data: list[str]) -> int:
    data = iter(data)
    board = BroadBoard(takewhile(lambda x: x != "\n", data))
    for move in chain.from_iterable(row.strip() for row in data):
        board.move_robot(move)
    return board.sum_gps()


if __name__ == "__main__":
    # with open("2024/data/example_15.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_15.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        # print(task_1(data_))
        print(task_2(data_))
