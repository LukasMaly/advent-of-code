import unittest
import os
import importlib

# Dynamically create a test case for each Python file
def create_test_case(puzzle):

    class TestPuzzle(unittest.TestCase):
        def test_part1(self):
            puzzle.test_part1()
        def test_part2(self):
            puzzle.test_part2()

    return TestPuzzle


# Discover and dynamically create test cases
def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    for filename in os.listdir('.'):
        if filename.endswith('.py') and filename != 'test_puzzles.py':
            day = importlib.import_module(filename[:-3])
            puzzle = day.Puzzle()
            test_case = create_test_case(puzzle)
            suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_case))
    return suite

if __name__ == "__main__":
    unittest.main()
