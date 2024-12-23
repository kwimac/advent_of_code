from typing import Any, Generator, Iterable


Point = tuple[int, int]

DIGITS_PAD_POSITIONS = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "3": (0, 2),
    "2": (1, 2),
    "1": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
}

MOVES_PAD_POSITIONS = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (1, 1),
}

def _translate_horizontal_fist(current_position: Point, destination: Point) -> Generator[str, Any, None]:
    x1, y1 = current_position
    x2, y2 = destination
    if x1 > x2:
        char = "<"
        x1, x2 = x2, x1
    else:
        char = ">"
    for _ in range(x2-x1):
        yield char
    if y1 > y2:
        char = "^"
        y1, y2 = y2, y1
    else:
        char = "v"
    for _ in range(y2-y1):
        yield char
    yield "A"

def _translate_vertical_first(current_position: Point, destination: Point) -> Generator[str, Any, None]:
    x1, y1 = current_position
    x2, y2 = destination
    if y1 > y2:
        char = "^"
        y1, y2 = y2, y1
    else:
        char = "v"
    for _ in range(y2-y1):
        yield char
    if x1 > x2:
        char = "<"
        x1, x2 = x2, x1
    else:
        char = ">"
    for _ in range(x2-x1):
        yield char
    yield "A"

def _parse(msg: Iterable[str], pad: dict[str, Point], horizontal_first: bool) -> Generator[str, Any, None]:
    position = pad["A"]
    for char in msg:
        destination = pad[char]
        translate = _translate_horizontal_fist if horizontal_first else _translate_vertical_first
        for symbol in translate(position, destination):
            yield symbol
        position = destination


def _get_shortest_combination_len(msg: str) -> int:
    shortest_combination_len = float("inf")
    for ii in range(8):
        f1, f2, f3 = (bool(int(x)) for x in f"{ii:03b}")
        print(f1, f2, f3)
        combination = "".join(
            _parse(
                _parse(
                    _parse(msg, DIGITS_PAD_POSITIONS, f1),
                    MOVES_PAD_POSITIONS,
                    f2,
                ),
                MOVES_PAD_POSITIONS,
                f3,
            )
        )
        print(msg, len(combination), combination)
        if len(combination) < shortest_combination_len:
            shortest_combination_len = len(combination)
    return shortest_combination_len


def task_1(data: list[str]) -> int:
    print([
        (int(row[:3]), _get_shortest_combination_len(row.strip()))
        for row in data
    ])
    return sum(
        int(row[:3]) * _get_shortest_combination_len(row.strip())
        for row in data
    )


def task_2(data: list[str]) -> int:
    ...


if __name__ == "__main__":
    with open("2024/data/example_21.txt", "r", encoding="utf-8") as _file:
    # with open("2024/data/input_21.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        print(task_1(data_))
        # print(task_2(data_))
