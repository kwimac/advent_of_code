from collections import Counter


def task_1(l1: list[int], l2: list[int]) -> int:
    return sum(
        abs(elem_1 - elem_2) 
        for elem_1, elem_2 
        in zip(sorted(l1), sorted(l2))
    )


def task_2(l1: list[int], l2: list[int]) -> int:
    d1 = Counter(l1)
    d2 = Counter(l2)
    sum_ = 0
    for k1, v1 in d1.items():
        if k1 in d2:
            sum_ += k1 * d2[k1] * v1
    return sum_


if __name__ == "__main__":
    # with open("data/example_01.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_01.txt", "r", encoding="utf-8") as _file:
        list_1, list_2 = zip(*(map(int, line.strip().split()) for line in _file))
    # print(task_1(list_1, list_2))
    print(task_2(list_1, list_2))
