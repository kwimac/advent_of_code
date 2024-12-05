def task_1(data: list[str]) -> int:
    ...


def task_2(data: list[str]) -> int:
    ...


if __name__ == "__main__":
    # with open("xxxx/data/example_xx.txt", "r", encoding="utf-8") as _file:
    with open("xxxx/data/input_xx.txt", "r", encoding="utf-8") as _file:
        data_ = _file.read().strip()
        print(task_1(data_))
        # print(task_2(data_))
