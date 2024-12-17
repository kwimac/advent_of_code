from collections import defaultdict
import heapq
from typing import Iterable

Point = tuple[int, int]
NodeState = tuple[int, Point, int]

class Maze:
    WALL_SYMBOL = "#"
    EMPTY_SYMBOL = "."
    START_POINT_SYMBOL = "S"
    END_POINT_SYMBOL = "E"
    DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
    STEP_SCORE = 1
    TURN_SCORE = 1000

    def __init__(self, maze: Iterable[str]) -> None:
        self.maze = [row.strip() for row in maze]
        n, m = len(maze), len(self.maze[0])
        self.start = (1, n-2)
        self.end = (m-2, 1)
        self.distance = {self.start: 0}
        self.prev = defaultdict(set)
        self._solve_maze()

    def _find_nodes(self, node_state: NodeState) -> list[NodeState]:
        to_check = [node_state]
        prev = node_state[-1]
        while len(to_check) == 1:
            score, p, direction, _ = to_check.pop()
            goes_straight = False
            for ii, straight in [
                (direction, True),
                ((direction-1)%4, False),
                ((direction+1)%4, False)
            ]:
                dx, dy = self.DIRECTIONS[ii]
                xx, yy = p[0]+dx, p[1]+dy
                if self.maze[yy][xx] != self.WALL_SYMBOL:
                    goes_straight ^= straight
                    new_score = score + self.STEP_SCORE + (0 if straight else self.TURN_SCORE)
                    to_check.append((new_score, (xx, yy), ii, p))
            if len(to_check) > 1 or p == self.end:
                if not goes_straight and p != self.end:
                    score += self.TURN_SCORE
                if (
                    p not in self.distance 
                    or score  <= self.distance[p]
                ):
                    self.distance[p] = score
                    if score  < self.distance[p]:
                        self.prev[p] = set()
                    self.prev[p].add(prev)
                    return [] if p == self.end else to_check
        return [] #  dead end, empty list
        
    def _solve_maze(self) -> None:
        to_check = [(0, self.start, 0, self.start)]
        while to_check:
            node_state = heapq.heappop(to_check)
            if node_state[0] <= self.distance.get(node_state[1], float("inf")):
                for node_state in self._find_nodes(node_state):
                    heapq.heappush(to_check, node_state)
    
    def get_solution(self) -> int:
        return self.distance.get(self.end, 0)
    
    def get_seats(self) -> int:
        if self.end not in self.prev:
            return 0
        visited = {self.end, self.start}
        seats = 0
        to_check = [self.end]
        while to_check:
            p = to_check.pop()
            d = self.distance[p]
            for pp in self.prev[p]:
                seats += (d - self.distance[pp]) % self.TURN_SCORE
                if pp not in visited:
                    to_check.append(pp)
                    visited.add(pp)
            seats -= len(self.prev[p]) - 1
        seats += 1
        return seats
        

def task_1(data: list[str]) -> int:
    return Maze(data).get_solution()


def task_2(data: list[str]) -> int:
    return Maze(data).get_seats()


if __name__ == "__main__":
    # with open("2024/data/example_16.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_16.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        # print(task_1(data_))
        print(task_2(data_))
