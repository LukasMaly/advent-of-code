import importlib
import os
from typing import List


class BasePuzzle:
    def __init__(self) -> None:
        self.input = self.__read_input(self.__get_input_file())

    def __get_input_file(self):
        file = str(importlib.import_module(self.__module__).__file__)
        dirname = os.path.dirname(file)
        basename = os.path.splitext(os.path.basename(file))[0]
        return os.path.join(dirname, 'inputs', basename + '.txt')

    def __read_input(self, file) -> List[str]:
        with open(file) as f:
            return f.read().splitlines()

    def part1(self, input: List[str]) -> int:
        raise NotImplementedError()

    def part2(self, input: List[str]) -> int:
        raise NotImplementedError()

    def run(self):
        print(self.part1(self.input[:]))
        print(self.part2(self.input[:]))
