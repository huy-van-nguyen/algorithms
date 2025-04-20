import unittest

class Solution:
    def contains_duplicate(self, numbers: list[int]) -> bool:
        seen = set()
        for number in numbers:
            if number in seen:
                return True
            seen.add(number)
        return False

class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_with_duplicates(self):
        self.assertTrue(self.solution.contains_duplicate([1, 2, 3, 1]))

    def test_without_duplicates(self):
        self.assertFalse(self.solution.contains_duplicate([1, 2, 3]))

    def test_empty(self):
        self.assertFalse(self.solution.contains_duplicate([]))

    def test_single_element(self):
        self.assertFalse(self.solution.contains_duplicate([42]))

    def test_all_duplicates(self):
        self.assertTrue(self.solution.contains_duplicate([5, 5, 5, 5]))

if __name__ == "__main__":
    unittest.main()
