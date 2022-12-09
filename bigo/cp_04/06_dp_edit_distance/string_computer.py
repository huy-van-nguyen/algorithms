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
    transform = []
    n = len(S)
    m = len(T)
    while n > 0 and m > 0:
        if S[n - 1] == T[m - 1]:
            n -= 1
            m -= 1
        elif f[n - 1][m - 1] == (f[n][m] - 1):
            transform.append('C{}{:0>2d}'.format(T[m-1], n))
            n -= 1
            m -= 1
        elif f[n - 1][m] == (f[n][m] - 1):
            transform.append('D{}{:0>2d}'.format(S[n-1], n))
            n -= 1
        else:
            transform.append('I{}{:0>2d}'.format(T[m-1], n+1))
            m -= 1
    while m > 0:
        transform.append('I{}{:0>2d}'.format(T[m-1], 1))
        m -= 1
    while n > 0:
        transform.append('D{}{:0>2d}'.format(S[n-1], n))
        n -= 1
    transform.append('E')
    return ''.join(transform)


def solve():
    # abcde bcgfe
    #
    # Da01Cg03If04E
    while True:
        string = input()
        if string == '#':
            break
        S, T = string.strip().split()
        global f
        f = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
        edit_distance(S, T)
        print(trace(S, T))


if __name__ == '__main__':
    solve()
