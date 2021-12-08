import glob
import importlib
import os
import sys

import pytest


dates = sorted(glob.glob('20??/??.py'))
dates = [date.split('/') for date in dates]
dates = [(date[0], os.path.splitext(date[1])[0]) for date in dates]

@pytest.mark.parametrize('part', ['part1', 'part2'])
@pytest.mark.parametrize('year, day', dates)
def test_puzzles(year, day, part):
    day = importlib.import_module(f"{year}.{day}")
    if part == 'part1':
        day.Puzzle().test_part1()
    else:
        day.Puzzle().test_part2()


if __name__ == '__main__':
    sys.exit(pytest.main())
