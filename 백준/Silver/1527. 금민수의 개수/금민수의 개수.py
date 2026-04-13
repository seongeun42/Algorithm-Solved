import sys
sys.setrecursionlimit(10**5)

def dfs(cur):
    if cur > B:
        return 0
    cnt = 0
    if A <= cur <= B:
        cnt = 1
    cnt += dfs(cur * 10 + 4)
    cnt += dfs(cur * 10 + 7)
    return cnt

A, B = map(int, input().split())
print(dfs(0))