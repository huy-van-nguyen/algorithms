import sys
import unittest


def smallest_difference(array_one, array_two):
    array_one.sort()
    array_two.sort()
    index_1, index_2, smallest = -1, -1, sys.maxsize
    i, j = 0, 0
    while i < len(array_one) and j < len(array_two):
        diff = abs(array_one[i] - array_two[j])
        if diff < smallest:
            index_1, index_2, smallest = i, j, diff
        if array_one[i] > array_two[j]:
            j += 1
        elif array_one[i] < array_two[j]:
            i += 1
        else:
            return [array_one[i], array_two[j]]
    for k in range(i, len(array_one)):
        diff = abs(array_one[k] - array_two[j-1])
        if diff < smallest:
            index_1, index_2, smallest = k, j-1, diff
    for k in range(j, len(array_two)):
        diff = abs(array_one[i-1] - array_two[k])
        if diff < smallest:
            index_1, index_2, smallest = i-1, k, diff

    return [array_one[index_1], array_two[index_2]]


class TestProgram(unittest.TestCase):
    def test_smallest_difference(self):
        array_one = [-1, 5, 10, 20, 28, 3]
        array_two = [26, 134, 135, 15, 17]
        expected = [28, 26]
        actual = smallest_difference(array_one, array_two)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
