import unittest


def binary_search(array, target):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


class TestProgram(unittest.TestCase):
    def test_binary_search(self):
        # array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        # target = 33
        # expected = 3
        array = [1, 5, 23, 111]
        target = 111
        expected = 3
        actual = binary_search(array, target)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
