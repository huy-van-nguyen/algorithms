import unittest


def longest_peak(array):
    found_peak = False
    start_mountain = 0
    end_mountain = -1
    longest = 0
    for i in range(1, len(array)):
        if not found_peak:
            if array[i - 1] > array[i]:
                if i - start_mountain >= 2:
                    end_mountain = i
                    found_peak = True
                else:
                    start_mountain = i
                    found_peak = False
                    end_mountain = -1
            elif array[i - 1] == array[i]:
                start_mountain = i
                found_peak = False
                end_mountain = -1
            else:
                continue
        else:
            if array[i - 1] > array[i]:
                end_mountain = i
            elif array[i-1] == array[i]:
                if longest < (end_mountain - start_mountain + 1):
                    longest = end_mountain - start_mountain + 1
                start_mountain = i
                found_peak = False
                end_mountain = -1
            else:
                if longest < (end_mountain - start_mountain + 1):
                    longest = end_mountain - start_mountain + 1
                start_mountain = i - 1
                found_peak = False
                end_mountain = -1
    if found_peak and end_mountain - start_mountain > 0:
        if longest < (end_mountain - start_mountain + 1):
            longest = end_mountain - start_mountain + 1

    return longest


class TestProgram(unittest.TestCase):
    def test_longest_peak(self):
        # array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
        # expected = 6

        # array = [1, 3, 2]
        # expected = 3

        array = [1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1]
        expected = 9
        actual = longest_peak(array)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
