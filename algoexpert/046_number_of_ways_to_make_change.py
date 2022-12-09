import unittest


def number_of_ways_to_make_change(target, coins):
    n = len(coins)
    # We need sum+1 rows as the table is constructed
    # in bottom up manner using the base case 0 value
    # case (sum = 0)
    table = [[0 for x in range(n)] for x in range(target + 1)]

    # Fill the entries for 0 value case (n = 0)
    for i in range(n):
        table[0][i] = 1

    # Fill rest of the table entries in bottom up manner
    for i in range(1, target + 1):
        for j in range(n):
            # Count of solutions including coins[j]
            x = table[i - coins[j]][j] if i - coins[j] >= 0 else 0

            # Count of solutions excluding coins[j]
            y = table[i][j - 1] if j >= 1 else 0

            # total count
            table[i][j] = x + y

    return table[target][n - 1]


class TestProgram(unittest.TestCase):
    def test_number_of_ways_to_make_change(self):
        # target amount of money
        target = 6
        # distinct positive integers coin
        coins = [1, 5]
        expected = 2
        actual = number_of_ways_to_make_change(target, coins)
        self.assertEqual(expected, actual)


if __name__ == '__name__':
    unittest.main()
