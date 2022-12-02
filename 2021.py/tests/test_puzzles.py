import glob
import importlib
import os
import sys

import pytest


days = sorted(glob.glob('??.py'))
days = [os.path.splitext(day)[0] for day in days]

@pytest.mark.parametrize('part', ['part1', 'part2'])
@pytest.mark.parametrize('day', days)
def test_puzzles(day, part):
    day = importlib.import_module(f"{day}")
    if part == 'part1':
        day.Puzzle().test_part1()
    else:
        day.Puzzle().test_part2()


if __name__ == '__main__':
    sys.exit(pytest.main())
