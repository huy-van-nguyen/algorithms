import unittest


def three_number_sum(array, target_sum):
    array.sort()
    triplets = []
    for i in range(len(array)):
        left = i + 1
        right = len(array) - 1
        while left < right:
            if array[left] + array[right] == target_sum - array[i]:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif array[left] + array[right] > target_sum - array[i]:
                right -= 1
            else:
                left += 1
    return triplets


class TestProgram(unittest.TestCase):
    def test_three_number_sum(self):
        array = [12, 3, 1, 2, -6, 5, -8, 6]
        target_number = 0
        expected = [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
        actual = three_number_sum(array, target_number)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
