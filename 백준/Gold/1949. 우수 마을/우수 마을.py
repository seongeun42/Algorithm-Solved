import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(cur, visited, town, dp):
    visited[cur] = True
    for nxt in town[cur]:
        if not visited[nxt]:
            super_town, normal_town = dfs(nxt, visited, town, dp)
            dp[cur][0] += normal_town
            dp[cur][1] += max(super_town, normal_town)
    return dp[cur]

def solve():
    N = int(input())
    population = [*map(int, input().split())]
    town = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        town[a].append(b)
        town[b].append(a)
    dp = [[0, 0]] + [[p, 0] for p in population]
    visited = [False] * (N + 1)
    dfs(1, visited, town, dp)
    print(max(sum(dp, [])))

solve()