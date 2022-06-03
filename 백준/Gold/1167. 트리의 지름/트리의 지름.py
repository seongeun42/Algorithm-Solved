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

V = int(input())
G = [[] for _ in range(V + 1)]
for _ in range(V):
    info = [*map(int, input().split())]
    for i in range(1, len(info) - 2, 2):
        G[info[0]].append((info[i], info[i + 1]))
visited = [0] * (V + 1)
max_v, far = 0, 1
dfs(1, 0)
visited = [0] * (V + 1)
dfs(far, 0)
print(max_v)