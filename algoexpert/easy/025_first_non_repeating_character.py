import unittest


def first_non_repeating_character(string):
    dict = {}
    for i in range(len(string)):
        if string[i] in dict:
            dict[string[i]] += 1
        else:
            dict[string[i]] = 1
    for i in range(len(string)):
        if dict[string[i]] == 1:
            return i
    return -1


class TestProgram(unittest.TestCase):
    def test_first_non_repeating_character(self):
        input = "abcdcaf"
        expected = 1
        actual = first_non_repeating_character(input)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()