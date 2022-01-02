
import unittest
from steps import SwappableSolution
from steps import get_result


class TestResult(unittest.TestCase):

    def test_1_simple_step(self):
        array_start = [3, 2, 1, 4]
        array_goal = [1, 2, 3, 4]
        actual = get_result(array_start, array_goal)
        expected = 1
        self.assertEqual(actual, expected)

    def test_2_simple_steps(self):
        array_start = [4, 5, 2, 3]
        array_goal = [5, 4, 3, 2]
        actual = get_result(array_start, array_goal)
        expected = 2
        self.assertEqual(actual, expected)

    def test_empty(self):
        array_start = []
        array_goal = []
        actual = get_result(array_start, array_goal)
        expected = 0
        self.assertEqual(actual, expected)

    def test_0_steps(self):
        array_start = [1, 2]
        array_goal = [1, 2]
        actual = get_result(array_start, array_goal)
        expected = 0
        self.assertEqual(actual, expected)

    def test_different_lenght_arrays(self):
        array_start = [1]
        array_goal = [1, 2]
        actual = get_result(array_start, array_goal)
        expected = 0
        self.assertEqual(actual, expected)

    def test_1_transitive_step(self):
        array_start = [2, 3, 1]
        # 2<=>3 -> 3, 2, 1
        # 3<=>1 -> 1, 2, 3
        array_goal = [1, 2, 3]
        actual = get_result(array_start, array_goal)
        expected = 2
        self.assertEqual(actual, expected)


class TestSwappableSolution(unittest.TestCase):

    def test_getSwapScore(self):
        array_start = [2, 1, 4, 5, 3]
        array_goal = [1, 2, 3, 4, 5]
        ss = SwappableSolution(array_start, array_goal)

        actual = ss.getSwapScore(0, 1)
        expected = 2
        self.assertEqual(actual, expected)

        actual = ss.getSwapScore(2, 3)
        expected = 1
        self.assertEqual(actual, expected)

        actual = ss.getSwapScore(0, 2)
        expected = 0
        self.assertEqual(actual, expected)

    def test_badPositions(self):
        array_start = [3, 2, 1, 4]
        array_goal = [1, 2, 3, 4]
        # findBadPositions() is implicitly called by a constructor of SwappableSolution
        ss = SwappableSolution(array_start, array_goal)
        actual = ss.bad_positions.positions
        expected = [0, 2]
        self.assertEqual(actual, expected)

    def test_countSwapsWithMaxScore(self):
        array_start = [3, 2, 1, 4, 6, 5]
        array_goal = [1, 2, 3, 4, 5, 6]
        # findBadPositions() is implicitly called by a constructor of SwappableSolution
        ss = SwappableSolution(array_start, array_goal)

        actual = ss.getSwapsWithMaxScore()
        expected = [(0, 2), (4, 5)]
        self.assertEqual(actual, expected)
