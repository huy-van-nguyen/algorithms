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


def solve():
    S = input()
    T = input()
    global f
    f = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
    print(edit_distance(S, T))


if __name__ == '__main__':
    solve()
