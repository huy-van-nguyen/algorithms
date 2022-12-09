import unittest


def bubble_sort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(1, len(array)):
            if array[j] < array[j - 1]:
                temp = array[j - 1]
                array[j - 1] = array[j]
                array[j] = temp
                swapped = True
        if not swapped:
            break
    return array


class TestProgram(unittest.TestCase):
    def test_bubble_sort(self):
        array = [8, 5, 2, 9, 5, 6, 3]
        expected = [2, 3, 5, 5, 6, 8, 9]
        actual = bubble_sort(array)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
