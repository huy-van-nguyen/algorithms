import unittest


def first_duplicate_value(array):
    s = set()
    for value in array:
        if value in s:
            return value
        else:
            s.add(value)
    return -1


class TestProgram(unittest.TestCase):
    def test_first_duplicate_value(self):
        input = [2, 1, 5, 2, 3, 3, 4]
        expected = 2
        actual = first_duplicate_value(input)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
