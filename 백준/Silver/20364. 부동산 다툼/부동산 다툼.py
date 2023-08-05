import sys
input = sys.stdin.readline

def dfs(pre, idx):
    if pre == 1:
        return idx
    parent = pre // 2
    if parent in live:
        idx = dfs(parent, parent)
    else:
        idx = dfs(parent, idx)
    return idx

n, q = map(int, input().split())
live = set()
live.add(int(input()))
print(0)
for _ in range(q - 1):
    x = int(input())
    res = dfs(x, 0 if x not in live else x)
    if res == 0:
        live.add(x)
    print(res)