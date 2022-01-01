
import unittest
import caves


class TestSolution(unittest.TestCase):

    def test_1(self):
        cave = [1, 2, -1]
        actual = caves.get_result(cave)
        expected = 0
        self.assertEqual(actual, expected)

    def test_2(self):
        cave = [1, -1, 1, 2]
        actual = caves.get_result(cave)
        expected = 3
        self.assertEqual(actual, expected)

    def test_loop(self):
        cave = [1, 0, 3, -1]
        actual = caves.get_result(cave)
        expected = 2
        self.assertEqual(actual, expected)
