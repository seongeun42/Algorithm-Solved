from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque([[1, 0]])
    visit[1] = 1
    ans = []
    cur_deg = 0
    while q:
        node, deg = q.popleft()
        if deg == cur_deg:
            ans.append(node)
        else:
            cur_deg = deg
            ans = [node]
        for n in G[node]:
            if not visit[n]:
                visit[n] = 1
                q.append([n, deg + 1])
    print(min(ans), cur_deg, len(ans))

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
visit = [0] * (N + 1)
bfs()