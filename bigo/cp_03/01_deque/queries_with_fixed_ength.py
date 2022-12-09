from collections import deque
import sys


n, q = map(int, input().split())
numbers = list(map(int, input().strip().split()))[:n]
dq = deque([])
while q > 0:
    d = int(input())
    dq.clear()
    best = sys.maxsize
    for i in range(0, n):
        while len(dq) > 0 and numbers[dq[-1]] < numbers[i]:
            dq.pop()
        dq.append(i)
        while len(dq) > 0 and dq[0] <= i - d:
            dq.popleft()
        if i >= d - 1:
            if best > numbers[dq[0]]:
                best = numbers[dq[0]]
    print(best)
    q -= 1