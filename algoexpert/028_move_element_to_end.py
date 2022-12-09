import unittest


def move_element_to_end(array, to_move):
    left = []
    for i in range(len(array)):
        if array[i] != to_move:
            left.append(array[i])
    for i in range(len(left)):
        array[i] = left[i]
    k = len(left)
    while k < len(array):
        array[k] = to_move
        k += 1
    return array


def move_element_to_end_optimal(array, to_move):
    i = 0
    while i < len(array):
        if array[i] == to_move:
            j = i + 1
            while i < len(array) and j < len(array):
                if array[j] == to_move:
                    j += 1
                else:
                    array[i], array[j] = array[j], array[i]
                    i += 1
                    j += 1
            if j == len(array):
                break
        i += 1
    return array


class TestProgram(unittest.TestCase):
    def test_move_element_to_end(self):
        array = [2, 1, 2, 2, 2, 3, 4, 2]
        to_move = 2
        expected_start = [1, 3, 4]
        expected_end = [2, 2, 2, 2, 2]
        # output = move_element_to_end(array, to_move)
        output = move_element_to_end_optimal(array, to_move)
        output_start = sorted(output[0:3])
        output_end = output[3:]
        self.assertEqual(expected_start, output_start)
        self.assertEqual(expected_end, output_end)


if __name__ == '__main__':
    unittest.main()
