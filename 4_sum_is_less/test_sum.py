import unittest
from sum import get_result
from sum import Solution, Log2xpk


class TestResult(unittest.TestCase):

    def test_1(self):
        arr = [3, 2, 4, 5]
        w = 9
        actual = get_result(arr, w)
        expected = True
        self.assertEqual(actual, expected)

    def test_2(self):
        arr = [3, 2, 4, 5]
        w = 6
        actual = get_result(arr, w)
        expected = False
        self.assertEqual(actual, expected)


class TestFindBestIndexToDevive(unittest.TestCase):

    def test_findBestIndexToDevive_1(self):
        arr = [8, 4, 4, 2, 1]
        s = Solution(arr)
        actual = s.findBestIndexToDevive()
        expected = 1
        self.assertEqual(actual, expected)

    def test_findBestIndexToDevive_2(self):
        arr = [8, 2, 1]
        s = Solution(arr)
        actual = s.findBestIndexToDevive()
        expected = 0
        self.assertEqual(actual, expected)


class TestFindMinumumSum(unittest.TestCase):
    def test_findMinumumSum_1(self):
        '''
step 1: devide 16
8 8 4 2 1 -> 8+15 = 23
step 2: devide 8
8 4 4 2 1 -> 8+11 = 19
step 3: devide 4
8 4 2 2 1 -> 8+9 = 17
step 4: devide 4
8 2 2 2 1 -> 8+7 = 15
step 5: devide 2
8 2 2 1 1 -> 8+6 = 14
step 6: devide 2
8 2 1 1 1 -> 8+5 = 13
step 7: devide 2
8 1 1 1 1 -> 8+4 = 12
step 8: devide 1
8 1 1 1 0 -> 8+3 = 11
'''
        arr = [16, 8, 4, 2, 1]
        s = Solution(arr)
        actual = s.findMinumumSum()
        expected = 11
        self.assertEqual(actual, expected)
