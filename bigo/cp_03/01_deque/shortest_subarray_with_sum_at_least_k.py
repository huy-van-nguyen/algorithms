from collections import deque

n, k = map(int, input().split())
numbers = list(map(int, input().strip().split()))

P = [0]
for i in range(0, n):
    P.append(P[-1] + numbers[i])
result = n + 1
dq = deque([])
for i in range(0, len(P)):
    while len(dq) > 0 and P[i] <= P[dq[-1]]:
        dq.pop()
    while len(dq) > 0 and P[i] - P[dq[0]] >= k:
        result = min(result, i - dq[0])
        dq.popleft()
    dq.append(i)
print(result if result < n + 1 else -1)

