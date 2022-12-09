import unittest


def is_monotonic(array):
    monotone_increasing = True
    for i in range(1, len(array)):
        if array[i-1] <= array[i]:
            continue
        else:
            monotone_increasing = False
            break

    monotone_decreasing = True
    for i in range(1, len(array)):
        if array[i - 1] >= array[i]:
            continue
        else:
            monotone_decreasing = False
            break
    if monotone_increasing or monotone_decreasing:
        return True
    return False


class TestProgram(unittest.TestCase):
    def test_is_monotonic(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        expected = True
        actual = is_monotonic(array)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
