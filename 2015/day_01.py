def task_1(data: str) -> int:
    return sum(-1 if char == ")" else 1 for char in data)


def task_2(data: str) -> int:
    level = 0
    for ii, char in enumerate(data, 1):
        level += -1 if char == ")" else 1
        if level < 0:
            return ii


if __name__ == "__main__":
    # with open("2015/data/example_01.txt", "r", encoding="utf-8") as _file:
    with open("2015/data/input_01.txt", "r", encoding="utf-8") as _file:
        data_ = _file.read().strip()
        print(task_1(data_))
        print(task_2(data_))
