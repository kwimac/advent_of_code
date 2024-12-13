from collections import Counter, defaultdict
from typing import Generator, Iterable


def _apply_rules(
    data: Iterable[tuple[str, int]],
) -> Generator[tuple[str, int], None, None]:
    for elem, count in data:
        if elem == "0":
            yield "1", count
        elif len(elem)%2 == 0:
            n = len(elem)//2
            yield elem[:n], count
            yield str(int(elem[n:])), count
        else:
            yield str(int(elem) * 2024), count

def task_1(data: list[str]) -> int:
    counter = {num: 1 for num in data[0].strip().split()}
    data = counter.items()
    for _ in range(25):
        counter = defaultdict(int)
        for num, ii in _apply_rules(data):
            counter[num] += ii
        data = counter.items()
    return sum(counter.values())


def task_2(data: list[str]) -> int:
    counter = Counter(data[0].strip().split())
    data = counter.items()
    for _ in range(75):
        counter = Counter()
        for num, ii in _apply_rules(data):
            counter[num] += ii
        data = counter.items()
    return sum(counter.values())


if __name__ == "__main__":
    # with open("2024/data/example_11.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_11.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        # print(task_1(data_))
        print(task_2(data_))
