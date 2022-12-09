import unittest


def minimum_waiting_time(queries):
    queries.sort()
    minimum = 0
    for index, query in enumerate(queries, start=1):
        minimum += (len(queries) - index) * queries[index - 1]
    return minimum


class TestProgram(unittest.TestCase):
    def test_minimum_waiting_time(self):
        queries = [3, 2, 1, 2, 6]
        expected = 17
        actual = minimum_waiting_time(queries)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
