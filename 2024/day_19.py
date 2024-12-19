from collections import defaultdict
from typing import Mapping



def _count_combinations(pattern: str, towels_map: Mapping[int, set[str]]) -> int:
    pattern = pattern.strip()
    combinations_num = [0] * (len(pattern) + 1)
    combinations_num[0] = 1
    for ii in range(1, len(combinations_num)):
        for towel_len, towels in towels_map.items():
            if (
                pattern[ii-towel_len:ii] in towels 
                and combinations_num[ii-towel_len]
            ):
                combinations_num[ii] += combinations_num[ii-towel_len]
    return combinations_num[-1]
    

def task_1(data: list[str]) -> int:
    data = iter(data)
    towels_map = defaultdict(set)
    for towel in next(data).strip().split(", "):
        towels_map[len(towel)].add(towel)
    next(data)
    return sum(int(_count_combinations(pattern.strip(), towels_map) != 0) for pattern in data)



def task_2(data: list[str]) -> int:
    data = iter(data)
    towels_map = defaultdict(set)
    for towel in next(data).strip().split(", "):
        towels_map[len(towel)].add(towel)
    next(data)
    return sum(_count_combinations(pattern.strip(), towels_map) for pattern in data)


if __name__ == "__main__":
    # with open("2024/data/example_19.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_19.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        print(task_1(data_))
        print(task_2(data_))
