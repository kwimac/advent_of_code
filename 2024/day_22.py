from collections import defaultdict, deque


NUMBER = 16777216-1

def _mix_and_prune(sn: int, value: int) -> int:
    return (sn^value)&NUMBER

def _get_next_number(sn: int) -> int:
    sn = _mix_and_prune(sn, sn<<6)
    sn = _mix_and_prune(sn, sn>>5)
    sn = _mix_and_prune(sn, sn<<11)
    return sn

def _get_nth_number(sn: int, n: int) -> int:
    for _ in range(n):
        sn = _get_next_number(sn)
    return sn

def task_1(data: list[str]) -> int:
    return sum(
        _get_nth_number(int(row.strip()), 2000)
        for row in data
    )

def _get_sell_options_for_nth(sn: int, n: int) -> dict[tuple[int, int, int, int], int]:
    if n < 4:
        return {}
    p_prev = sn % 10
    sequence = deque([])
    for _ in range(4):
        sn = _get_next_number(sn)
        p_curr = sn % 10
        sequence.append(p_curr - p_prev)
        p_prev = p_curr
    options = {tuple(sequence): p_curr}
    for _ in range(n-4):
        sn = _get_next_number(sn)
        p_curr = sn % 10
        sequence.append(p_curr - p_prev)
        p_prev = p_curr
        sequence.popleft()
        key = tuple(sequence)
        if key not in options:
            options[key] = p_curr
    return options


def task_2(data: list[str]) -> int:
    options_total_price = defaultdict(int)
    for row in data:
        for option, price in _get_sell_options_for_nth(int(row.strip()), 2000).items():
            options_total_price[option] += price
    return max(options_total_price.values())


if __name__ == "__main__":
    # with open("2024/data/example_22.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_22.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        # print(task_1(data_))
        print(task_2(data_))
