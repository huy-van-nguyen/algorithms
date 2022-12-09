import unittest


def non_constructible_change(coins):
    coins.sort()
    sum = 0
    for i in range(len(coins)):
        if sum + 1 < coins[i]:
            return sum + 1
        else:
            sum += coins[i]
    return sum + 1


class TestProgram(unittest.TestCase):
    def test_non_constructible_change(self):
        input = [5, 7, 1, 1, 2, 3, 22]
        expected = 20
        actual = non_constructible_change(input)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
