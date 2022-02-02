from collections import deque
import sys
input = sys.stdin.readline

def bfs(node):
    q = deque([node])
    res[node] = 0
    while q:
        v = q.popleft()
        for i in m[v]:
            if res[i] == -1:
                res[i] = res[v] + 1
                q.append(i)

N, M, K, X = map(int, input().split())
m = [[] for _ in range(N+1)]
res = [-1] * (N+1)
for _ in range(M):
    n1, n2 = map(int, input().split())
    m[n1].append(n2)
bfs(X)
isExist = False
for i, v in enumerate(res):
    if v == K:
        isExist = True
        print(i)
if not isExist: print(-1)