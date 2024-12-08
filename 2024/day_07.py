from pyparsing import deque


def _parse_line(line: str) -> tuple[int, list[str]]:
    result, values = line.split(":")
    result = int(result.strip())
    values = values.split()
    return result, values

def _process_line(result: int, values: list[str]) -> int:
    operators = {
        '+': lambda x, y: x+int(y),
        '*': lambda x, y: x*int(y),
    }
    n = len(values)
    val = int(values[0])
    states = deque([(val, 1, '+'), (val, 1, '*')])
    while states:
        val, ii, operator = states.popleft()
        if ii<n:
            val = operators[operator](val, values[ii])
            if val == result:
                return result
            if val > result:
                continue
            states.extend((val, ii+1, operator) for operator in operators)
    return 0


def task_1(data: list[str]) -> int:
    return sum(_process_line(*_parse_line(line)) for line in data)


def _process_line_2(result: int, values: list[str]) -> int:
    operators = {
        '+': lambda x, y: int(x)+int(y),
        '*': lambda x, y: int(x)*int(y),
        '||': lambda x, y: int(x+y),
    }
    n = len(values)
    val = values[0]
    states = deque([(val, 1, '+'), (val, 1, '*'), (val, 1, '||')])
    while states:
        val, ii, operator = states.popleft()
        if ii<n:
            val = operators[operator](val, values[ii])
            if val == result:
                return result
            if val > result:
                continue
            states.extend((str(val), ii+1, operator) for operator in operators)
    return 0


def task_2(data: list[str]) -> int:
    return sum(_process_line_2(*_parse_line(line)) for line in data)


if __name__ == "__main__":
    # with open("2024/data/example_07.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_07.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        # print(task_1(data_))
        print(task_2(data_))
