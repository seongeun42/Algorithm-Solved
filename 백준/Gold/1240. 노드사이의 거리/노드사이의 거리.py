from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, end):
    q = deque([start])
    visit[start] = 1
    while q:
        node = q.popleft()
        if node == end:
            break
        for n, w in G[node]:
            if not visit[n]:
                visit[n] = visit[node] + w
                q.append(n)

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    n1, n2, w = map(int, input().split())
    G[n1].append((n2, w))
    G[n2].append((n1, w))

for _ in range(M):
    visit = [0] * (N + 1)
    s, e = map(int, input().split())
    bfs(s, e)
    print(visit[e] - 1)