from _collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    visited = [0] * (n + 1)
    q = deque([(s, 0)])
    visited[s] = 1
    score = 0
    while q:
        node, cnt = q.popleft()
        score = max(score, cnt)
        for next in G[node]:
            if visited[next] == 0:
                q.append((next, cnt + 1))
                visited[next] = 1
    return score

n = int(input())
G = [[] for _ in range(n + 1)]
while 1:
    a, b = map(int, input().split())
    if a == b == -1: break
    G[a].append(b)
    G[b].append(a)

scores = []
for i in range(1, n + 1):
    scores.append((i, bfs(i)))

scores.sort(key=lambda x: (x[1], x[0]))
minV = scores[0][1]
scores = [v for v in scores if v[1] == minV]

print(minV, len(scores))
print(*[v[0] for v in scores])