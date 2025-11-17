import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur, G, visited):
    visited[cur] = True
    cnt = 1
    for nxt in G[cur]:
        if not visited[nxt]:
            cnt += dfs(nxt, G, visited)
    return cnt

def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, input().split())
        G[B].append(A)
    X = int(input())
    visited = [False] * (N + 1)
    print(dfs(X, G, visited) - 1)

solve()