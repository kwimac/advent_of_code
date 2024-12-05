from collections import defaultdict


def _check_row(rules: dict[int, set[int]], row: list[int]) -> int:
    for ii, elem in enumerate(row):
        if (rule := rules.get(elem)) and rule.intersection(row[:ii]):
            return 0
    return row[len(row)//2]


def task_1(rules: dict[int, int], data: list[int]) -> int:
    return sum(_check_row(rules, row) for row in data)


def _check_row_2(rules: dict[int, set[int]], row: list[int]) -> int:
    _modified = False
    for ii, elem in enumerate(row):
        if rule := rules.get(elem):
            if to_fix := rule.intersection(row[:ii]):
                _modified = True
                jj = ii
                while jj > 0 and to_fix:
                    row[jj] = row[jj-1]
                    to_fix.discard(row[jj])
                    jj -= 1
                row[jj] = elem
    return row[len(row)//2] if _modified else 0


def task_2(rules: dict[int, int], data: list[int]) -> int:
    return sum(_check_row_2(rules, row) for row in data)


if __name__ == "__main__":
    # with open("2024/data/example_05.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_05.txt", "r", encoding="utf-8") as _file:
        file_iter = iter(_file)
        line = next(file_iter)
        rules_: dict[int, set[int]] = defaultdict(set)
        while line != "\n":
            key, val = map(int, line.strip().split('|'))
            rules_[key].add(val)
            line = next(file_iter)
        data_ = [list(map(int, line.strip().split(","))) for line in file_iter]
        rules_ = dict(rules_)
    print(task_1(rules_, data_))
    print(task_2(rules_, data_))
