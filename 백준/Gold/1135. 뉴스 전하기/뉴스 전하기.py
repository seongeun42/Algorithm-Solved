def dfs(cur, tree):
    nexts = sorted([dfs(nxt, tree) for nxt in tree[cur]])
    cnt = len(nexts)
    return max([0] + [nexts[i] + cnt - i for i in range(cnt)])

def solve():
    N = int(input())
    boss = [*map(int, input().split())]
    tree = [[] for _ in range(N)]
    for i in range(1, N):
        tree[boss[i]].append(i)
    print(dfs(0, tree))

solve()