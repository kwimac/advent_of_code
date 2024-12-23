from collections import defaultdict
from functools import reduce
from typing import Any, Generator


EdgesMap = dict[str, set[str]]

def _create_edges_map(data: list[str]) -> EdgesMap:
    edges_map = defaultdict(set)
    for row in data:
        v1, v2 = row.strip().split("-")
        edges_map[v1].add(v2)
        edges_map[v2].add(v1)
    return edges_map

def _find_triplets(edges_map: EdgesMap) -> set[tuple[str, str, str]]:
    triplets = set()
    for v1, vertices1 in edges_map.items():
        if v1[0] == "t":
            for v2 in vertices1:
                for v3 in edges_map[v2]:
                    if v1 in edges_map[v3]:
                        triplets.add(tuple(sorted([v1,v2,v3])))
    return triplets

def task_1(data: list[str]) -> int:
    edges_map = _create_edges_map(data)
    return (len(_find_triplets(edges_map)))


def _find_cliques(cliques: tuple[str, ...], edges_map: EdgesMap) -> Generator[tuple[str, ...], Any, None]:
    for clique in cliques:
        common_vertices = reduce(lambda x, y: x&edges_map[y], clique[1:], edges_map[clique[0]])
        for v in common_vertices:
            yield tuple(sorted([v, *clique]))


def task_2(data: list[str]) -> str:
    edges_map = _create_edges_map(data)
    cliques = _find_triplets(edges_map)
    prev = None
    while cliques:
        prev = cliques
        cliques = set(_find_cliques(cliques, edges_map))
    return ",".join(sorted(prev.pop()))


if __name__ == "__main__":
    # with open("2024/data/example_23.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_23.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        # print(task_1(data_))
        print(task_2(data_))
