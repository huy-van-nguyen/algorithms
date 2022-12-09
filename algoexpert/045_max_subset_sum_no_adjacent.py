import unittest


def max_subset_sum_no_adjacent(array):
    dp = [[0 for i in range(2)] for i in range(len(array))]
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    dp[0][0] = 0  # giá trị lớn nhất tại phần tử thứ ith mà ko chọn array[i]
    dp[0][1] = array[0]  # giá trị lớn nhất tại phần tử thứ ith mà chọn array[i]
    for i in range(1, len(array)):
        dp[i][1] = dp[i - 1][0] + array[i]
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
    return max(dp[len(array) - 1][0], dp[len(array) - 1][1])


def max_subset_sum_no_adjacent_optimal(array):
    excluded = 0
    included = 0
    for i in range(len(array)):
        # Current max excluding i
        new_excluded = max(included, excluded)
        # Current max including i
        included = excluded + array[i]
        excluded = new_excluded
    return max(included, excluded)


class TestProgram(unittest.TestCase):
    def test_max_subset_sum_no_adjacent(self):
        array = [75, 105, 120, 75, 90, 135]
        expected = 330
        actual = max_subset_sum_no_adjacent(array)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
