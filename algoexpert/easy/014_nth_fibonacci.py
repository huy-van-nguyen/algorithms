import unittest


def get_nth_fib(n):
    f0 = 0
    f1 = 1
    if n == 1:
        return f0
    if n == 2:
        return f1
    for _ in range(2, n):
        fn = f0 + f1
        f0 = f1
        f1 = fn
    return fn


class TestProgram(unittest.TestCase):
    def test_get_nth_fib(self):
        n = 6
        expected = 5
        actual = get_nth_fib(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
