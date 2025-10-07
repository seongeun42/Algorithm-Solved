import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(cur, G, visited, total):
    visited[cur] = True
    dist = total
    for nxt, d in G[cur]:
        if not visited[nxt]:
            dist = max(dist, dfs(nxt, G, visited, total + d))
    return dist

def solve():
    N = int(input())
    G = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        A, B, C = map(int, input().split())
        G[A].append((B, C))
        G[B].append((A, C))
    print(dfs(1, G, [False] * (N + 1), 0))

solve()