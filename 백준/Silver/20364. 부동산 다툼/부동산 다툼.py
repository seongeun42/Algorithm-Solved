import sys
input = sys.stdin.readline

def dfs(pre, idx, live):
    if pre == 1:
        return idx
    parent = pre // 2
    if parent in live:
        idx = dfs(parent, parent, live)
    else:
        idx = dfs(parent, idx, live)
    return idx

def solve(q):
    live = {int(input())}
    print(0)
    for _ in range(q - 1):
        x = int(input())
        res = dfs(x, 0 if x not in live else x, live)
        if res == 0:
            live.add(x)
        print(res)

if __name__ == "__main__" :
    n, q = map(int, input().split())
    solve(q)