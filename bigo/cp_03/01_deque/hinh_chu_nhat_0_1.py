m, n = map(int, input().split())
matrix = []
H = [0 for x in range(0, n + 1)]
L = [0 for x in range(0, n + 1)]
R = [0 for x in range(0, n + 1)]
T = [0 for x in range(0, n + 1)]
matrix.append(T)
for i in range(1, m + 1):
    arr = list(map(int, input().strip().split()))
    matrix.append([0] + arr)
max_area = 0
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if matrix[i][j] == 1:
            H[j] += 1
        else:
            H[j] = 0
    stack = []
    for j in range(1, n + 1):
        while len(stack) > 0 and H[stack[0]] >= H[j]:
            stack.pop()
        if len(stack) == 0:
            L[j] = 1
        else:
            L[j] = stack[0] + 1
        stack.append(j)
    stack.clear()
    for j in range(n, 0, -1):
        while len(stack) > 0 and H[stack[0]] >= H[j]:
            stack.pop()
        if len(stack) == 0:
            R[j] = n
        else:
            R[j] = stack[0] - 1
            stack.append(j)
    for j in range(1, n + 1):
        max_area = max(max_area, (R[j] - L[j] + 1) * H[j])
print(H)
print(max_area)


