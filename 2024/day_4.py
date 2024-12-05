import re


def task_1(data: list[str]) -> int:
    m, n = len(data), len(data[0])

    def check_x(ii: int, jj: int) -> int:
        result = 0
        for r, c in [
            (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1)
        ]:
            x, y = ii, jj
            _match = True
            for char in 'MAS':
                x += r
                y += c
                if not(0<=x<m and 0<=y<n and data[x][y] == char):
                    _match = False
                    break
            if _match:
                result += 1
        return result

    return sum(
        check_x(ii, match_.start())
        for ii in range(m)
        for match_ in re.finditer('X', data[ii])
    )   


def task_2(data: list[str]) -> int:
    m, n = len(data), len(data[0])

    def check_x(ii: int, jj: int) -> int:
        result = 0
        for chars in ['SMMS', 'MMSS', 'MSSM', 'SSMM']:
            _match = True
            for char, (r, c) in zip(chars, [(1,1), (-1,1), (-1,-1), (1,-1)]):
                x, y = ii+r, jj+c
                if not(0<=x<m and 0<=y<n and data[x][y] == char):
                    _match = False
                    break
            if _match:
                result += 1
        return result

    return sum(
        check_x(ii, match_.start())
        for ii in range(m)
        for match_ in re.finditer('A', data[ii])
    )   


if __name__ == "__main__":
    # with open("data/example_04.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_04.txt", "r", encoding="utf-8") as _file:
        data_ = [line_.strip() for line_ in _file]
        print(task_1(data_))
        print(task_2(data_))
