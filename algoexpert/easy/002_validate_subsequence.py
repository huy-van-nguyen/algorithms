import unittest


def is_valid_subsequence(array, sequence):
    if len(array) < len(sequence):
        return False
    index_of_array = 0
    index_of_sequence = 0
    while index_of_array < len(array) and index_of_sequence < len(sequence):
        if array[index_of_array] == sequence[index_of_sequence]:
            index_of_sequence += 1
        index_of_array += 1
    return index_of_sequence == len(sequence)


class TestProgram(unittest.TestCase):
    def test_valid_subsequence_return_true(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(is_valid_subsequence(array, sequence))


if __name__ == '__main__':
    unittest.main()

# python -m unittest 002_validate_subsequence.py
