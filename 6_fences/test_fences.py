import unittest
from fences import get_result


class TestResult(unittest.TestCase):

    def test_1(self):
        fences = [0, 2, 4, 1, 6, 2]
        actual = get_result(fences)
        expected = True
        self.assertEqual(actual, expected)

    def test_2(self):
        fences = [2, -1, 0, 2]
        actual = get_result(fences)
        expected = True
        self.assertEqual(actual, expected)

    def test_3(self):
        # 7.458s
        fences = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        actual = get_result(fences)
        expected = False
        self.assertEqual(actual, expected)
