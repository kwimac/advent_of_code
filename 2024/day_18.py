import heapq
import pprint
from typing import Generator

Point = tuple[int, int]
NodeState = tuple[int, Point, int]

class Board:
    EMPTY_SYMBOL = "."
    WALL_SYMBOL = "#"
    DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]

    def __init__(self, k: int, data: list[str], n_first: int) -> None:
        self.board = self.initialize_board(k, data, n_first)
        self.distances = {}

    def initialize_board(self, k: int, data: list[str], n_first: int) -> list[list[str]]:
        n, m = k+2, k+2
        board = [
            [self.WALL_SYMBOL for _ in range(m)],
            *(
                [self.EMPTY_SYMBOL for _ in range(m)] 
                for _ in range(n-2)
            ),
            [self.WALL_SYMBOL for _ in range(m)],
        ]
        for ii in range(1, n-1):
            board[ii][0] = self.WALL_SYMBOL
            board[ii][-1] = self.WALL_SYMBOL
        for row in data[:n_first]:
            x, y = map(int, row.strip().split(","))
            board[y+1][x+1] = self.WALL_SYMBOL
        return board

    def solve(self) -> int:
        to_check = [(0, (1,1), 0)]
        while to_check:
            score, point, direction = heapq.heappop(to_check)
            if score < self.distances.get(point, float("inf")):
                self.distances[point] = score
                for node_state in self._traverse(score, point, direction):
                    heapq.heappush(to_check, node_state)
        n = len(self.board)-2
        return self.distances.get((n, n), 0)

    def _traverse(
        self,
        score: int,
        point: Point, 
        direction: int
    ) -> Generator[NodeState, None, None]:
        for ii in [direction, (direction-1)%4, (direction+1)%4]:
            dx, dy = self.DIRECTIONS[ii]
            xx, yy = point[0]+dx, point[1]+dy
            if self.board[yy][xx] != self.WALL_SYMBOL:
                yield(score+1, (xx, yy), ii)


def task_1(data: list[str]) -> int:
    board = Board(71, data, 1024)
    return board.solve()


def task_2(data: list[str]) -> int:
    for ii in range(1024, len(data)):
        if Board(71, data, ii).solve() == 0:
            break
    return data[ii-1].strip()


if __name__ == "__main__":
    # with open("2024/data/example_18.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_18.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        # print(task_1(data_))
        print(task_2(data_))
