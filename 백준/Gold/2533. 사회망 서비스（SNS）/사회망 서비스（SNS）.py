import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(pre, cur, G):
    cur_ea, cur_no_ea = 1, 0
    for nxt in G[cur]:
        if nxt == pre:
            continue
        nxt_ea, nxt_no_ea = dfs(cur, nxt, G)
        cur_ea += min(nxt_ea, nxt_no_ea)
        cur_no_ea += nxt_ea
    return cur_ea, cur_no_ea

def solve():
    N = int(input())
    G = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    print(min(dfs(0, 1, G)))

solve()