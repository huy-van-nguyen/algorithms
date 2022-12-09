def solve():
    t = int(input())
    while t > 0:
        n = int(input())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        diff = abs(sum(a) - sum(b))
        operations = diff
        i = 0
        while diff > 0:
            if a[i] != b[i]:
                a[i] = b[i]
                diff -= 1
            i += 1
        equal = True
        for j in range(n):
            if a[j] != b[j]:
                equal = False
                break
        if equal:
            print(operations)
        else:
            print(operations+1)
        t -= 1


if __name__ == '__main__':
    solve()