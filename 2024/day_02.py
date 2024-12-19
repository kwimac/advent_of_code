from typing import Iterable


def _check_row(row: list[int], is_inc: bool) -> int:
    for e1, e2 in zip(row[0:-1], row[1:]):
        if not (0 < e2-e1 < 4 if is_inc else -4 < e2-e1 < 0):
            return 0
    return 1


def task_1(data: Iterable[list[int]]) -> int:
    return sum(_check_row(row, (row[1] - row[0]) > 0) for row in data)

def _check_row_2(row: list[int]) -> bool:
    if _check_row(row, (row[1] - row[0]) > 0):
        return True
    return any(
        _check_row(_row, (_row[1] - _row[0]) > 0)
        for ii in range(0, len(row))
        if (_row:=row[:ii] + row[ii+1:])
    )


def task_2(data: Iterable[list[int]]) -> int:
    return sum(int(_check_row_2(row)) for row in data)


if __name__ == "__main__":
    # with open("2024/data/example_02.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_02.txt", "r", encoding="utf-8") as _file:
        data_ = (list(map(int, line.strip().split())) for line in _file)
        # print(task_1(data_))
        print(task_2(data_))
