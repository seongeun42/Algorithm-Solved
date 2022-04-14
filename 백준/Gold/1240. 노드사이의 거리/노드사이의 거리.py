from collections import deque
import sys
input = sys.stdin.readline

def dfs(node, dist, end):
    visit[node] = dist
    for n, w in G[node]:
        if n == end:
            visit[end] = dist + w
            break
        if not visit[n]:
            dfs(n, dist + w, end)

def bfs(start, end):
    q = deque([[start, 1]])
    visit[start] = 1
    while q:
        node, dist = q.popleft()
        for n, w in G[node]:
            if n == end:
                visit[end] = dist + w
                break
            if not visit[n]:
                q.append([n, dist + w])

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    n1, n2, w = map(int, input().split())
    G[n1].append((n2, w))
    G[n2].append((n1, w))

for _ in range(M):
    visit = [0] * (N + 1)
    s, e = map(int, input().split())
    dfs(s, 1, e)
    # bfs(s, e)
    print(visit[e] - 1)