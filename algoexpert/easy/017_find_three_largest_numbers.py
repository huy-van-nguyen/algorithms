import unittest


def find_three_largest_numbers(array):
    three_largest = [array[0], array[1], array[2]]
    three_largest.sort(reverse=True)
    largest_1 = three_largest[0]
    largest_2 = three_largest[1]
    largest_3 = three_largest[2]
    for i in range(3, len(array)):
        if array[i] > largest_1:
            largest_3 = largest_2
            largest_2 = largest_1
            largest_1 = array[i]
        elif array[i] > largest_2:
            largest_3 = largest_2
            largest_2 = array[i]
        elif array[i] > largest_3:
            largest_3 = array[i]
    return [largest_3, largest_2, largest_1]


class TestProgram(unittest.TestCase):
    def test_find_three_largest_numbers(self):
        array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
        expected = [18, 141, 541]
        actual = find_three_largest_numbers(array)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()