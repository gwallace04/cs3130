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

    def test_with_10_integers(self):
        input_list = [56, 18, 51, 6, 93, 6, 37, 57, 87, 67]
        self._test_all_funcs(input_list)

if __name__ == "__main__":
    unittest.main()
