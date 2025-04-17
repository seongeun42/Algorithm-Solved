def dfs(cur, tree):
    nexts = sorted([dfs(nxt, tree) for nxt in tree[cur]])
    cnt = len(nexts)
    if cnt == 0:
        return 0
    for i in range(cnt):
        nexts[i] += cnt - i
    return max(nexts)

def solve():
    N = int(input())
    boss = [*map(int, input().split())]
    tree = [[] for _ in range(N)]
    for i in range(1, N):
        tree[boss[i]].append(i)
    print(dfs(0, tree))

solve()