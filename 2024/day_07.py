def _process_line(line: str) -> int:
    result, values = line.split(":")
    result = int(result.strip())
    values = list(map(int, values.split()))

    n_bits = len(values)
    for ii in range(2**n_bits-1):
        value = values[0]
        for val, char in zip(values[1:], f"{ii:b}".zfill(n_bits)):
            value = value + val if char == "0" else value * val
        if value == result:
            return result
    return 0


def task_1(data: list[str]) -> int:
    return sum(_process_line(line) for line in data)


def task_2(data: list[str]) -> int:
    ...


if __name__ == "__main__":
    # with open("2024/data/example_07.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_07.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        print(task_1(data_))
        # print(task_2(data_))
