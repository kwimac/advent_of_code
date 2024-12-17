from collections import deque
import re
from typing import Generator

def _parse_data(data: list[str]) -> tuple[int, int, int, list[int]]:
    pattern = r".*: ([0-9,]+)"
    data = iter(data)
    A = int(re.match(pattern, next(data)).group(1))
    B = int(re.match(pattern, next(data)).group(1))
    C = int(re.match(pattern, next(data)).group(1))
    next(data)
    program = list(map(int, re.match(pattern, next(data)).group(1).split(",")))
    return A, B, C, program

 
def execute(A: int, B: int, C: int, program: list[int]) -> list[int]:
    def _execute(A: int, B: int, C: int, program: list[int]) -> Generator[int, None, None]:
        def get_combo(operand: int) -> int:
            if operand == 4:
                return A
            if operand == 5:
                return B
            if operand == 6:
                return C
            return operand
        p = 0
        while p < len(program):
            op, val = program[p], program[p+1]
            if op==0:
                A = A // 2**get_combo(val)
                p += 2
            elif op==1:
                B ^= val
                p += 2
            elif op==2:
                B = get_combo(val) % 8
                p += 2
            elif op==3:
                p = p+2 if A == 0 else val
            elif op==4:
                B = B ^ C
                p += 2
            elif op==5:
                yield get_combo(val) % 8
                p += 2
            elif op==6:
                B = A // 2**get_combo(val)
                p += 2
            elif op==7:
                C = A // 2**get_combo(val)
                p += 2
    return list(_execute(A, B, C, program))


def task_1(data: list[str]) -> str:
    return ",".join(map(str, execute(*_parse_data(data))))


def task_2(data: list[str]) -> int:
    A, B, C, program = _parse_data(data)
    number = ""
    n = len(program)
    to_check = deque([("", 1)])
    while to_check:
        number, jj = to_check.popleft()
        for ii in range(8):
            digit = f"{ii:03b}"
            A = int(number+digit, 2)
            if execute(A, B ,C, program) == program[-jj:]:
                if jj+1 > n:
                    return A
                to_check.append((number+digit, jj+1))



if __name__ == "__main__":
    # with open("2024/data/example_17.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_17.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        # print(task_1(data_))
        print(task_2(data_))
