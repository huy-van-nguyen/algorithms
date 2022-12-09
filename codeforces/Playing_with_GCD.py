def gcd_extended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcd_extended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def lcm(a, b):
    gcd, x, y = gcd_extended(a, b)
    return (a * b) / gcd


def solve():
    t = int(input())
    while t > 0:
        n = int(input())
        a = list(map(int, input().strip().split()))
        b = [0 for _ in range(n+1)]
        b[0] = a[0]
        for i in range(0, n - 1):
            b[i+1] = lcm(a[i], a[i + 1])
        b[n] = a[n-1]
        result = 'YES'
        for i in range(n):
            gcd, x, y = gcd_extended(b[i], b[i+1])
            if gcd != a[i]:
                result = 'NO'
                break
        print(result)
        t -= 1


if __name__ == '__main__':
    solve()