import sys
sys.setrecursionlimit(10**6)

def dfs(cur, tree, praise, visited):
    visited[cur] = True
    for nxt in tree[cur]:
        if not visited[nxt]:
            praise[nxt] += praise[cur]
            dfs(nxt, tree, praise, visited)

def solve():
    n, m = map(int, input().split())
    boss = [*map(int, input().split())]
    tree = [[] for _ in range(n + 1)]
    for i in range(n):
        tree[boss[i]].append(i + 1)
    praise = [0] * (n + 1)
    for _ in range(m):
        i, w = map(int, input().split())
        praise[i] += w
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        dfs(i, tree, praise, visited)
    print(*praise[1:])

solve()