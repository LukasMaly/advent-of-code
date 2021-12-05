import glob
import os
import sys

import pytest


DAYS = [os.path.splitext(os.path.basename(day))[0] for day in sorted(glob.glob('2021/day*.py'))]


@pytest.mark.parametrize('part', ['part1', 'part2'])
@pytest.mark.parametrize('day', DAYS)
def test_days(day, part):
    exec(f'from {day} import Puzzle')
    exec(f'Puzzle().test_{part}()')


if __name__ == '__main__':
    sys.exit(pytest.main())
