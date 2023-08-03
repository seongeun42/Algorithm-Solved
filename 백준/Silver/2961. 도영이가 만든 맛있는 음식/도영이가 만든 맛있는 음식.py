import sys
input = sys.stdin.readline

def dfs(dep, s, b):
    global ans
    if dep == n:
        if s != 0 and ans > abs(s - b):
            ans = abs(s - b)
        return
    dfs(dep + 1, s * sb[dep][0] if s else sb[dep][0], b + sb[dep][1])
    dfs(dep + 1, s, b)

n = int(input())
sb = [[*map(int, input().split())] for _ in range(n)]
ans = 1000000000
dfs(0, 0, 0)
print(ans)