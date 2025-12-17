import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur, G, visited, fan):
    if cur in fan:
        return False
    if len(G[cur]) == 0:
        return True
    for nxt in G[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            if dfs(nxt, G, visited, fan):
                return True
    return False

def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
    S = int(input())
    fan = set([*map(int, input().split())])
    visited = [False] * (N + 1)
    visited[1] = True
    print("yes" if dfs(1, G, visited, fan) else "Yes")

solve()