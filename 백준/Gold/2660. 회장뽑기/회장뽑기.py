from _collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    visited = [0] * (n + 1)
    q = deque([s])
    visited[s] = 1
    while q:
        node = q.popleft()
        for next in G[node]:
            if visited[next] == 0:
                q.append(next)
                visited[next] = visited[node] + 1
    return max(visited) - 1

n = int(input())
G = [[] for _ in range(n + 1)]
while 1:
    a, b = map(int, input().split())
    if a == b == -1: break
    G[a].append(b)
    G[b].append(a)

score = 50
candi = []
for i in range(1, n + 1):
    s = bfs(i)
    if s < score:
        score = s
        candi = [i]
    elif s == score:
        candi.append(i)

print(score, len(candi))
print(*candi)