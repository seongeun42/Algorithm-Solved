import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(node, path):
    global cnt
    leaf = 1
    visited[node] = 1
    for n in G[node]:
        if not visited[n]:
            leaf = 0
            dfs(n, path + 1)
    if leaf:
        cnt += path

N = int(input())
G = [[] for _ in range(N + 1)]
cnt = 0
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
visited = [0] * (N + 1)
dfs(1, 0)
print("Yes" if cnt % 2 else "No")