import unittest


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while array[j] > key and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j+1] = key
    return array


class TestProgram(unittest.TestCase):
    def test_insertion_sort(self):
        array = [8, 5, 2, 9, 5, 6, 3]
        expected = [2, 3, 5, 5, 6, 8, 9]
        actual = insertion_sort(array)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()