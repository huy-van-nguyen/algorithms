from collections import deque

test_cases = int(input())
dq = deque([])
result = []
while test_cases > 0:
    n, k = map(int, input().split())
    numbers = list(map(int, input().strip().split()))[:n]
    dq.clear()
    result.clear()
    for i in range(0, n):
        if len(dq) > 0 and dq[0] <= i - k:
            dq.popleft()
        while len(dq) > 0 and numbers[dq[-1]] <= numbers[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(numbers[dq[0]])
    # print(*result, sep=' ')
    print(' '.join(map(str, result)))
    test_cases -= 1
