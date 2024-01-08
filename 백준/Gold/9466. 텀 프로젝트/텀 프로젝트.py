import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node, mark):
    visit[node] = mark
    if node == s[node]:
        return -1
    if visit[s[node]] == mark:
        return s[node]
    if visit[s[node]] == 0:
        res = dfs(s[node], mark)
        if res == node:
            return -1
        elif res == -1:
            visit[node] = -1
            return -1
        else:
            return res
    visit[node] = -1
    return -1

T = int(input())
for _ in range(T):
    n = int(input())
    s = [0] + [*map(int, input().split())]
    visit = [0] * (n + 1)
    for i in range(1, n + 1):
        if visit[i] == 0:
            dfs(i, i)
    print(visit.count(-1))