from itertools import takewhile
import re

class Device:
    def __init__(self, data: list[str]) -> None:
        self._values = {}
        self._gates = {}
        self._parse_data(data)

    def get_number(self) -> int:
        return int(
            "".join(
                str(self._get(key))
                for key in sorted(
                    (key for key in self._gates if key.startswith("z")),
                    reverse=True,
                )
            ),
            2,
        )
            
    def _parse_data(self, data) -> None:
        data = iter(data)
        for row in takewhile(lambda row: row.strip(), data):
            key, val = row.split(": ")
            self._values[key] = int(val)
        pattern = r"(\w+) (\w+) (\w+) -> (\w+)"
        self._gates = {
            key: (operator, v1, v2)
            for v1, operator, v2, key 
            in (
                re.match(pattern, row.strip()).groups()
                for row in data
            )
        }

    def _get(self, key: str) -> int:
        if key not in self._values:
            self._values[key] = self._solve(*self._gates[key])
        return self._values[key]

    def _solve(self, operator: str, v1_key: str, v2_key: str) -> int:
        v1 = self._get(v1_key)
        v2 = self._get(v2_key)
        if operator == "AND":
            return v1 & v2
        elif operator == "OR":
            return v1 | v2
        elif operator == "XOR":
            return v1 ^ v2

def task_1(data: list[str]) -> int:
    return Device(data).get_number()
        


def task_2(data: list[str]) -> int:
    ...


if __name__ == "__main__":
    # with open("2024/data/example_24.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_24.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        print(task_1(data_))
        # print(task_2(data_))
