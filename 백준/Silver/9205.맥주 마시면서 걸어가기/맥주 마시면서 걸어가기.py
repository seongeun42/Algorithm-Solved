import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(node):
    visited[node] = 1
    for i, v in enumerate(d):
        if not visited[i] and abs(d[node][0] - v[0]) + abs(d[node][1] - v[1]) <= 1000:
            dfs(i)

t = int(input())
for _ in range(t):
    n = int(input())
    d = [[*map(int, input().split())] for _ in range(n + 2)]
    visited = [0] * (n + 2)
    dfs(0)
    print("happy" if visited[-1] else "sad")