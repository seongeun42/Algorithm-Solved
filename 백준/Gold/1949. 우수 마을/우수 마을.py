import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(pre, cur, population, town):
    cur_superior, cur_normal = population[cur - 1], 0
    for nxt in town[cur]:
        if nxt == pre:
            continue
        nxt_superior, nxt_normal = dfs(cur, nxt, population, town)
        cur_superior += nxt_normal
        cur_normal += max(nxt_superior, nxt_normal)
    return cur_superior, cur_normal

def solve():
    N = int(input())
    population = [*map(int, input().split())]
    town = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        town[a].append(b)
        town[b].append(a)
    print(max(dfs(0, 1, population, town)))

solve()