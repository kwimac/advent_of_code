from typing import Iterable


def _check_row(row: list[int], is_inc: bool) -> int:
    for e1, e2 in zip(row[0:-1], row[1:]):
        if not (0 < e2-e1 < 4 if is_inc else -4 < e2-e1 < 0):
            return 0
    return 1


def task_1(data: Iterable[list[int]]) -> int:
    return sum(_check_row(row, (row[1] - row[0]) > 0) for row in data)


def _check_pair(e1: int, e2: int) -> str | None:
    if 0 < e2-e1 < 4:
        return '+'
    elif -4 < e2-e1 < 0:
        return '-'
    return None

k=0

def _check_row_2(row: list[int]) -> bool:
    l_row = len(row)
    ii = 1
    sign_l = _check_pair(row[ii-1], row[ii])
    if sign_l:
        ii += 1
        while ii < l_row:
            if _check_pair(row[ii-1], row[ii]) != sign_l:
                break
            ii += 1
        if ii >= l_row-1:
            return True
    jj = l_row-1
    sign_r = _check_pair(row[jj-1], row[jj])
    if sign_r:
        jj -= 1
        while jj > 0:
            if _check_pair(row[jj-1], row[jj]) != sign_r:
                break
            jj -= 1
        if jj <= 1:
            return True
    if jj - ii < 2 and sign_l == sign_r === _check_pair(row[jj-2], row[jj]):
        global k
        k+= 1
        print(k, row, jj)
        return True
    return False

# def _check_row_2(row: list[int]) -> bool:
#     if _check_row(row, (row[1] - row[0]) > 0):
#         return True
#     return any(
#         _check_row(_row, (_row[1] - _row[0]) > 0)
#         for ii in range(0, len(row))
#         if (_row:=row[:ii] + row[ii+1:])
#     )


def task_2(data: Iterable[list[int]]) -> int:
    return sum(int(_check_row_2(row)) for row in data)


if __name__ == "__main__":
    # with open("data/example_02.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_02.txt", "r", encoding="utf-8") as _file:
        data_ = (list(map(int, line.strip().split())) for line in _file)
        # print(task_1(data_))
        print(task_2(data_))
