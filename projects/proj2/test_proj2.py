import unittest

from proj2 import bubble
from proj2 import selection


class TestSortingAlgs(unittest.TestCase):

    def _test_single_func(self, func, input_list):
        expected_list = sorted(input_list)
        self.assertEqual(func(input_list), expected_list)

    def _test_all_funcs(self, input_list):
        self._test_single_func(bubble, input_list)
        self._test_single_func(selection, input_list)

    def test_with_empty_list(self):
        input_list = []
        self._test_all_funcs(input_list)

    def test_with_random_integers(self):
        input_list = [56, 18, 51, 6, 93, 6, 37, 57, 87, 67]
        self._test_all_funcs(input_list)

    def test_with_sorted(self):
        input_list = [i for i in range(10)]
        self._test_all_funcs(input_list)

    def test_with_almost_sorted(self):
        input_list = [46, 1, 2, 55, 4, 5, 87, 7, 8, 64] 
        self._test_all_funcs(input_list)

    def test_with_reverse_sorted(self):
        input_list = [i for i in range(10, 0, -1)] 
        self._test_all_funcs(input_list)

    def test_with_all_same(self):
        input_list = [1 for i in range(10)]
        self._test_all_funcs(input_list)

if __name__ == "__main__":
    unittest.main()
