import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def dfs(node, total):
    visited[node] = 1
    global max_v, far
    if total > max_v:
        max_v = total
        far = node
    for v, w in G[node]:
        if not visited[v]:
            dfs(v, total + w)

n = int(input())
G = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    n1, n2, w = map(int, input().split())
    G[n1].append((n2, w))
    G[n2].append((n1, w))
visited = [0] * (n + 1)
max_v, far = 0, 1
dfs(1, 0)
visited = [0] * (n + 1)
dfs(far, 0)
print(max_v)