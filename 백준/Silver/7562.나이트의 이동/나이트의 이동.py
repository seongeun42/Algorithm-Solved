from collections import deque

def bfs():
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    q = deque([[cur[0], cur[1]]])
    while q:
        v = q.popleft()
        if v == des:
            return m[v[1]][v[0]]
        for i in range(8):
            a, b = v[0] + dx[i], v[1] + dy[i]
            if 0 <= a < l and 0 <= b < l:
                if m[b][a] == 0:
                    m[b][a] = m[v[1]][v[0]] + 1
                    q.append([a, b])

t = int(input())
for _ in range(t):
    l = int(input())
    cur = list(map(int, input().split()))
    des = list(map(int, input().split()))
    m = [[0] * l for _ in range(l)]
    print(bfs())