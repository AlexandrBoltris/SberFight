import unittest
from robin_hood import get_result


class TestResult(unittest.TestCase):

    def test_1(self):
        passersby = [3, 10, 4, 8]
        actual = get_result(passersby)
        expected = 11
        self.assertEqual(actual, expected)

    def test_2(self):
        passersby = [5, 12, 6]
        actual = get_result(passersby)
        expected = 7
        self.assertEqual(actual, expected)
