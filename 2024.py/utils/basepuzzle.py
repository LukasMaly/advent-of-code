import importlib
import os

import yaml

from utils.timeit import timeit


class BasePuzzle:

    def __init__(self) -> None:
        self.lines = self.__read_input(self.__get_input_file())
        self.example = self.__read_example(self.__get_example_file())

    def __get_input_file(self) -> str:
        file = str(importlib.import_module(self.__module__).__file__)
        dirname = os.path.dirname(file)
        basename = os.path.splitext(os.path.basename(file))[0]
        return os.path.join(dirname, 'inputs', basename + '.txt')

    def __read_input(self, file) -> list[str]:
        with open(file) as f:
            return f.read().splitlines()

    def __get_example_file(self) -> str:
        file = str(importlib.import_module(self.__module__).__file__)
        dirname = os.path.dirname(file)
        basename = os.path.splitext(os.path.basename(file))[0]
        return os.path.join(dirname, 'examples', basename + '.yaml')

    def __read_example(self, file) -> dict:
        with open(file) as f:
            data = yaml.safe_load(f)
            data['input'] = data['input'].splitlines()
            return data

    def part1(self, lines: list[str]) -> int:
        raise NotImplementedError()

    def part2(self, lines: list[str]) -> int:
        raise NotImplementedError()

    @timeit
    def run_part1(self) -> int:
        return self.part1(self.lines[:])

    @timeit
    def run_part2(self) -> int:
        return self.part2(self.lines[:])

    # @timeit
    def test_part1(self):
        assert self.part1(self.example['input']) == self.example['answer1']

    # @timeit
    def test_part2(self):
        assert self.part2(self.example['input']) == self.example['answer2']

    def run(self):
        answer1 = self.run_part1()
        print(f"Part one answer: {answer1}")
        answer2 = self.run_part2()
        print(f"Part two answer: {answer2}")
