def longestCommonSubstring(X, Y, m, n):
    maxLength = 0
    endingIndex = m

    lookup = [[0 for x in range(n + 1)] for y in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1

                if lookup[i][j] > maxLength:
                    maxLength = lookup[i][j]
                    endingIndex = i

    return X[endingIndex - maxLength: endingIndex]


if __name__ == '__main__':
    # Exit Code 137 - Out of memory
    X = str(input())
    Y = str(input())

    m = len(X)
    n = len(Y)

    print(len(longestCommonSubstring(X, Y, m, n)))