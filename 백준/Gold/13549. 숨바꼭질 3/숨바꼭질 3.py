from collections import deque

def bfs():
    q = deque([N])
    a[N] = 0
    while q:
        v = q.popleft()
        if v == K:
            return a[K]
        if 0 <= 2 * v < 100001 and a[2 * v] == -1:
            a[2 * v] = a[v]
            q.appendleft(2 * v)
        if 0 <= v - 1 < 100001 and a[v - 1] == -1:
            a[v - 1] = a[v] + 1
            q.append(v - 1)
        if 0 <= v + 1 < 100001 and a[v + 1] == -1:
            a[v + 1] = a[v] + 1
            q.append(v + 1)


N, K = map(int, input().split())
a = [-1] * 100001
print(bfs())