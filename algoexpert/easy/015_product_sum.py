import unittest


def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def product_sum_with(array, level, sum):
    for value in array:
        if type(value) is int:
            sum += factorial(level) * value
        elif type(value) is list:
            level += 1
            sum = product_sum_with(value, level, sum)
            level -= 1
    return sum


def product_sum_optimal(array, level=1):
    sum = 0
    for value in array:
        if type(value) is int:
            sum += value
        elif type(value) is list:
            sum += product_sum_optimal(value, level + 1)
    return sum * level


def product_sum(array):
    return product_sum_with(array, 1, 0)


class TestProgram(unittest.TestCase):
    def test_product_sum(self):
        test = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
        expected = 12
        actual = product_sum(test)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
