import unittest


def edit_distance(S, T):
    '''
    modify S to T
    :param S:
    :param T:
    :return:
    '''
    for i in range(len(T) + 1):
        f[0][i] = i
    for i in range(len(S) + 1):
        f[i][0] = i
    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i - 1] == T[j - 1]:
                f[i][j] = f[i - 1][j - 1]
            else:
                f[i][j] = min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1]) + 1
    return f[len(S)][len(T)]


def trace(S, T):
    n = len(S)
    m = len(T)
    while n > 0 and m > 0:
        if S[n - 1] == T[m - 1]:
            n -= 1
            m -= 1
        elif f[n - 1][m - 1] == f[n][m] - 1:
            print('Replace {} {}'.format(n, T[m - 1]))
            n -= 1
            m -= 1
        elif f[n - 1][m] == f[n][m] - 1:
            print('Delete {}'.format(n))
            n -= 1
        else:
            print('Insert {} {}'.format(n + 1, T[m - 1]))
            m -= 1
    while m > 0:
        m -= 1
        print('Insert 1 {}'.format(T[m]))
    while n > 0:
        print('Delete {}'.format(n))
        n -= 1


class TestProgram(unittest.TestCase):
    def test_edit_distance(self):
        S = 'ACGGTATCA'
        T = 'TACGTATAC'
        global f
        f = [[0]*(len(T)+1) for _ in range(len(S)+1)]
        expected = 4
        actual = edit_distance(S, T)
        trace(S, T)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
