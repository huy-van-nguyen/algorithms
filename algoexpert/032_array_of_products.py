import unittest


def array_of_products(array):
    left_products = [0]*len(array)
    right_products = [0]*len(array)
    left_products[0] = array[0]
    for i in range(1, len(array)):
        left_products[i] = array[i] * left_products[i - 1]

    right_products[len(array) - 1] = array[len(array) - 1]
    for i in range(len(array) - 2, -1, -1):
        right_products[i] = array[i] * right_products[i + 1]

    products = [0]*len(array)
    for i in range(len(array)):
        left, right = 1, 1
        if i-1 >= 0:
            left = left_products[i-1]
        if i+1 < len(array):
            right = right_products[i+1]
        products[i] = left * right
    return products


class TestProgram(unittest.TestCase):
    def test_array_of_products(self):
        array = [5, 1, 4, 2]
        expected = [8, 40, 10, 20]
        actual = array_of_products(array)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
