def solve():
    t = int(input())
    while t > 0:
        n = int(input())
        a = list(map(int, input().strip().split()))
        for i in range(n):
            a[i] -= i
        a.sort()
        l = 0
        for i in range(n):
            if a[i] < 0:
                l = i
                break
        print((n-l) * (n-l-1))

        t -= 1


if __name__ == '__main__':
    solve()