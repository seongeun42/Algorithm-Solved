import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(pre, cur, G):
    police, no_police = 1, 0
    for nxt in G[cur]:
        if nxt == pre:
            continue
        nxt_police, nxt_no_police = dfs(cur, nxt, G)
        police += min(nxt_police, nxt_no_police)
        no_police += nxt_police
    return police, no_police

def solve():
    N = int(input())
    G = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    print(min(dfs(0, 1, G)))

solve()