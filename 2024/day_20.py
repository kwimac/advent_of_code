from collections import defaultdict
from functools import cached_property
import heapq
from typing import Any, Generator


Point = tuple[int, int]
NodeState = tuple[int, Point, int]

class Maze:
    EMPTY_SYMBOL = "."
    WALL_SYMBOL = "#"
    DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
    START_SYMBOL =  "S"
    END_SYMBOL = "E"

    def __init__(self, data: list[str]) -> None:
        self.board = [row.strip() for row in data]
        self.start, self.end = self._find_start_and_end()
        self._distances = {}
        self._prevs = defaultdict(set)
        self._shortcuts = defaultdict(set)

    @cached_property
    def _board_size(self) -> tuple[int, int]:
        return len(self.board), len(self.board[0])
    
    def _find_start_and_end(self) -> tuple[Point, Point]:
        start, end = None, None
        n, m = self._board_size
        for y in range(n):
            for x in range(m):
                if self.board[y][x] == self.START_SYMBOL:
                    start = (x, y)
                elif self.board[y][x] == self.END_SYMBOL:
                    end = (x, y)
                else:
                    continue
                if start and end:
                    return start, end
    
    def solve(self) -> int:
        to_check = [(0, self.start, 0)]
        while to_check:
            score, point, direction = heapq.heappop(to_check)
            if score < self._distances.get(point, float("inf")):
                self._distances[point] = score
                for node_state in self._traverse(score, point, direction):
                    heapq.heappush(to_check, node_state)
        return self._distances.get(self.end)

    def _traverse(
        self,
        score: int,
        point: Point,
        direction: int,
    ) -> Generator[NodeState, None, None]:
        n, m = self._board_size
        x, y = point
        for ii in [direction, (direction-1)%4, (direction+1)%4]:
            dx, dy = self.DIRECTIONS[ii]
            xx, yy = x+dx, y+dy
            next_score = self._distances.get((xx, yy), float("inf"))
            if self.board[yy][xx] != self.WALL_SYMBOL:
                if score+1 == next_score:
                    self._prevs[(xx, yy)].add((x,y))
                elif score+1 < next_score:
                    self._prevs[(xx, yy)] = {(x,y)}
                yield(score+1, (xx, yy), ii)
            elif (
                    0<=(yy:=y+2*dy)<n and 0<=(xx:=x+2*dx)<m
                    and self.board[yy][xx] != self.WALL_SYMBOL
                ):
                    self._shortcuts[point].add((xx,yy))

    def get_cheats(self) -> int:
        paths = set(self._get_paths())
        cheats = defaultdict(int)
        for point in paths:
            for point_2 in self._shortcuts[point]:
                if point_2 in paths and self._distances[point_2] > self._distances[point]:
                    cheats[self._distances[point_2] - self._distances[point]-2] += 1
        return cheats


    def _get_paths(self) -> Generator[Point, Any, None]:
        to_check = [self.end]
        while to_check:
            point = to_check.pop()
            if point == self.start:
                continue
            yield point
            for point in self._prevs[point]:
                to_check.append(point)
        yield self.start


def task_1(data: list[str]) -> int:
    maze = Maze(data)
    maze.solve()
    cheats = maze.get_cheats()
    return sum(num_ for len_, num_ in cheats.items() if len_>=100)


def task_2(data: list[str]) -> int:
    ...


if __name__ == "__main__":
    # with open("2024/data/example_20.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_20.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        print(task_1(data_))
        # print(task_2(data_))
