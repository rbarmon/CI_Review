

import unittest



class TestContainsDuplicate(unittest.TestCase):
    def test_contains_duplicate_true(self):
        self.assertTrue(contains_duplicate([1, 2, 3, 3]))

    def test_contains_duplicate_false(self):
        self.assertFalse(contains_duplicate([1, 2, 3, 4]))

    def test_empty_list(self):
        self.assertFalse(contains_duplicate([]))

    def test_single_element(self):
        self.assertFalse(contains_duplicate([1]))

    def test_all_duplicates(self):
        self.assertTrue(contains_duplicate([5, 5, 5, 5]))

if __name__ == "__main__":
    unittest.main()