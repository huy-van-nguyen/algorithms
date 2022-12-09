import unittest


def spiral_traverse(array):
    if len(array) < 0:
        return []
    spiral = []
    starting_row = 0
    ending_row = len(array) - 1
    starting_column = 0
    ending_column = len(array[0]) - 1

    while starting_column <= ending_row and starting_column <= ending_column:
        # left to right
        for i in range(starting_column, ending_column + 1):
            spiral.append(array[starting_row][i])
        starting_row += 1
        if starting_row > ending_row:
            break
        # top to down
        for i in range(starting_row, ending_row + 1):
            spiral.append(array[i][ending_column])
        ending_column -= 1
        if starting_column > ending_column:
            break
        # right to left
        for i in range(ending_column, starting_column - 1, -1):
            spiral.append(array[ending_row][i])
        ending_row -= 1
        # down to top
        for i in range(ending_row, starting_row - 1, -1):
            spiral.append(array[i][starting_column])
        starting_column += 1
    return spiral


class TestProgram(unittest.TestCase):
    def test_spiral_traverse(self):
        matrix = [[1, 2, 3, 4],
                  [12, 13, 14, 5],
                  [11, 16, 15, 6],
                  [10, 9, 8, 7]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        actual = spiral_traverse(matrix)
        self.assertEqual(expected, actual)

    def test_spiral_traverse_8(self):
        matrix = [[1, 2, 3, 4],
                  [10, 11, 12, 5],
                  [9, 8, 7, 6]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        actual = spiral_traverse(matrix)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
