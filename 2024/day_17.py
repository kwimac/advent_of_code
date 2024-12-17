import re


class Debugger:
    def __init__(self, data: list[str]) -> None:
        self._parse_input(data)
        self._operations_map = {
            0: self._adv,
            1: self._bxl,
            2: self._bst,
            3: self._jnz,
            4: self._bxc,
            5: self._out,
            6: self._bdv,
            7: self._cdv,
        }
        self._output = []

    def _parse_input(self, data: list[str]) -> None:
        pattern = r".*: ([0-9,]+)"
        data = iter(data)
        self.a = int(re.match(pattern, next(data)).group(1))
        self.b = int(re.match(pattern, next(data)).group(1))
        self.c = int(re.match(pattern, next(data)).group(1))
        next(data)
        self.program = list(map(int, re.match(pattern, next(data)).group(1).split(",")))
    
    def execute(self) -> str:
        pointer = 0
        while pointer < len(self.program):
            result = self._operations_map[self.program[pointer]](self.program[pointer+1])
            pointer = result if result is not None else pointer+2
        return ",".join(map(str, self._output))

    def _map_operand(self, operand: int) -> int:
        if operand == 4:
            return self.a
        if operand == 5:
            return self.b
        if operand == 6:
            return self.c
        return operand

    def _adv(self, operand: int) -> None:
        self.a //= 2**self._map_operand(operand)

    def _bxl(self, operand: int) -> None:
        self.b ^= operand

    def _bst(self, operand: int) -> None:
        self.b = self._map_operand(operand) % 8

    def _jnz(self, operand: int) -> int | None:
        if self.a != 0:
            return operand
    
    def _bxc(self, _: int) -> None:
        self.b ^= self.c
    
    def _out(self, operand: int) -> None:
        self._output.append(self._map_operand(operand)%8)

    def _bdv(self, operand: int) -> None:
        self.b //= 2**self._map_operand(operand)

    def _cdv(self, operand: int) -> None:
        self.c //= 2**self._map_operand(operand)


def task_1(data: list[str]) -> str:
    return Debugger(data).execute()


def task_2(data: list[str]) -> int:
    ...


if __name__ == "__main__":
    # with open("2024/data/example_17.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_17.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        print(task_1(data_))
        # print(task_2(data_))
