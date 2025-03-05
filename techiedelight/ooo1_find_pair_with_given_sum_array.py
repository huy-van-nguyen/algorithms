# Function to find a pair in an array with a given sum using hashing
import unittest


def find_pair(arr, target):
    # create an empty dictionary
    d = {}
    # do for each element
    for index, element in enumerate(arr):
        # check if pair (element, target - element) exists
        # if the deference is seen before, print the pair
        diff = target - element
        if diff in d:
            # print('Pair found', (diff, arr[index]))
            return diff, arr[index]
            # store index of the current element in the dictionary
        d[element] = index
    # No pair with the given sum exists in the list
    print("Pair not found")
    return None


class TestFindPair(unittest.TestCase):
    def test_pair_found(self):
        self.assertEqual(find_pair([8, 7, 2, 5, 3, 1], 10), (8, 2))
        self.assertEqual(find_pair([4, 6, 3, 8], 9), (6, 3))

    def test_pair_not_found(self):
        self.assertIsNone(find_pair([1, 2, 3, 4], 10))
        self.assertIsNone(find_pair([], 5))


if __name__ == '__main__':
    unittest.main()
