import queue

#

MAX = 100
INF = 10e9


def bfs(source, target):
    q = queue.Queue()
    q.put(source)
    global level
    level = [-1] * MAX
    level[source] = 0
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if level[v] != -1:
                continue
            if cap[u][v] <= flow[u][v]:
                continue
            level[v] = level[u] + 1
            q.put(v)
    return level[target] != -1


def dfs(source, target, pushed):
    if pushed == 0:
        return 0
    if source == target:
        return pushed
    start = iterate[source]
    stop = len(graph[source])
    for i in range(start, stop):
        v = graph[source][i]
        if level[v] != level[source] + 1:
            continue
        if cap[source][v] <= flow[source][v]:
            continue
        f = min(pushed, cap[source][v] - flow[source][v])
        f = dfs(v, target, f)
        if f == 0:
            continue
        flow[source][v] += f
        flow[v][source] -= f
        return f
    return 0


# source: source
# target: sink
def dinic(source, target):
    new_flow, sum_flow = 0, 0
    while bfs(source, target):
        global iterate
        iterate = [0] * MAX
        new_flow = dfs(source, target, INF)
        while new_flow > 0:
            sum_flow += new_flow
            new_flow = dfs(source, target, INF)
    return sum_flow


if __name__ == '__main__':
    cap = [[0 for i in range(MAX)] for i in range(MAX)]
    flow = [[0 for i in range(MAX)] for i in range(MAX)]
    iterate = [0] * MAX
    level = [-1] * MAX
    graph = [[] for i in range(MAX)]

    source, target = 0, 0
    E = int(input())
    for i in range(E):
        x, y, z = input().strip().split()
        u = ord(x) - 65
        v = ord(y) - 65
        w = int(z)
        if x == 'S':
            source = u
        if y == 'T':
            target = v
        graph[u].append(v)
        graph[v].append(u)
        cap[u][v] = w
    if source != target:
        print(dinic(source, target))
