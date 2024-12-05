from operator import mul
import re


def task_1(data: str) -> int:
    pattern = r"mul\((\d{0,3}),(\d{0,3})\)"
    return sum(
        mul(*map(int, elem.groups()))
        for elem in re.finditer(pattern, data)
    )


def task_2(data: list[str]) -> int:
    pattern = r"mul\((\d{0,3}),(\d{0,3})\)|(do\(\))|(don't\(\))"
    matches = re.finditer(pattern, data)
    match_ = next(matches, None)
    mul_ = True
    result = 0
    while match_:
        match_ = match_.groups()
        if match_[3]:
            mul_ = False
        elif match_[2]:
            mul_ = True
        else:
            if mul_:
                try:
                    result += int(match_[0]) * int(match_[1])
                except ValueError:
                    print(match_)
        match_ = next(matches, None)
    return result


if __name__ == "__main__":
    # with open("data/example_03.txt", "r", encoding="utf-8") as _file:
    with open("data/input_03.txt", "r", encoding="utf-8", newline='\r') as _file:
        data_ = _file.read().strip()
        # print(task_1(data_))
        print(task_2(data_))
