import unittest


def is_palindrome(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


class TestProgram(unittest.TestCase):
    def test_is_palindrome(self):
        string = 'abcdcba'
        expected = True
        actual = is_palindrome(string)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
