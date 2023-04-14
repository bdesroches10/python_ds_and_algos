import unittest

from binary_search import binary_search


class TestSearch(unittest.TestCase):
    def test_mid_even(self):
        # find value at beginning of array
        arr = [1, 3, 7, 9, 10, 14, 23, 34]
        query = 9
        results = binary_search(arr, query)
        self.assertEqual(results, 3)

    def test_mid_odd(self):
        # find value at beginning of array
        arr = [1, 3, 7, 9, 10, 14, 23]
        query = 9
        results = binary_search(arr, query)
        self.assertEqual(results, 3)

    def test_front(self):
        # find value at beginning of array
        arr = [1, 3, 7, 9, 10, 14, 23, 34]
        query = 1
        results = binary_search(arr, query)
        self.assertEqual(results, 0)

    def test_end(self):
        # find value at beginning of array
        arr = [1, 3, 7, 9, 10, 14, 23, 34]
        query = 34
        results = binary_search(arr, query)
        self.assertEqual(results, 7)

    def test_none(self):
        # find value at beginning of array
        arr = [1, 3, 7, 9, 10, 14, 23, 34]
        query = 2
        results = binary_search(arr, query)
        self.assertEqual(results, -1)


if __name__ == '__main__':
    unittest.main()
