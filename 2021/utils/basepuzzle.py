import importlib
import os
from typing import Dict, List

import yaml


class BasePuzzle:
    def __init__(self) -> None:
        self.input = self.__read_input(self.__get_input_file())
        self.example = self.__read_example(self.__get_example_file())

    def __get_input_file(self) -> str:
        file = str(importlib.import_module(self.__module__).__file__)
        dirname = os.path.dirname(file)
        basename = os.path.splitext(os.path.basename(file))[0]
        return os.path.join(dirname, 'inputs', basename + '.txt')

    def __read_input(self, file) -> List[str]:
        with open(file) as f:
            return f.read().splitlines()

    def __get_example_file(self) -> str:
        file = str(importlib.import_module(self.__module__).__file__)
        dirname = os.path.dirname(file)
        basename = os.path.splitext(os.path.basename(file))[0]
        return os.path.join(dirname, 'examples', basename + '.yaml')

    def __read_example(self, file) -> Dict:
        with open(file) as f:
            data = yaml.safe_load(f)
            data['input'] = data['input'].splitlines()
            return data

    def part1(self, input: List[str]) -> int:
        raise NotImplementedError()

    def part2(self, input: List[str]) -> int:
        raise NotImplementedError()

    def test_part1(self):
        assert self.part1(self.example['input']) == self.example['answer1']

    def test_part2(self):
        assert self.part2(self.example['input']) == self.example['answer2']

    def run(self):
        print(self.part1(self.input[:]))
        print(self.part2(self.input[:]))
