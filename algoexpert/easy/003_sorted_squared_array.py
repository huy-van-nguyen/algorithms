import unittest


def sorted_squared_array(array):
    for i in range(0, len(array)):
        array[i] = pow(array[i], 2)
    array.sort()
    return array


def sorted_squared_array_optimal(array):
    squared_array = [0 for _ in range(0, len(array))]
    left = 0
    right = len(array) - 1
    idx = len(array) - 1
    while left <= right:
        if abs(array[left]) > abs(array[right]):
            squared_array[idx] = pow(array[left], 2)
            left += 1
        else:
            squared_array[idx] = pow(array[right], 2)
            right -= 1
        idx -= 1
    return squared_array


class TestProgram(unittest.TestCase):
    def test_sorted_squared_array(self):
        input = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = sorted_squared_array(input)
        self.assertEqual(expected, actual)

    def test_sorted_squared_array_optimal(self):
        input = [-2, -1]
        expected = [1, 4]
        actual = sorted_squared_array_optimal(input)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()