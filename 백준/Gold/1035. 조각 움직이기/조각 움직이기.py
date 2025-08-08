from itertools import permutations
import sys
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def is_connected(idxs):
    visited = set()
    def dfs(cur):
        cnt = 1
        visited.add(cur)
        for d in range(4):
            nr, nc = cur[0] + dr[d], cur[1] + dc[d]
            if (nr, nc) in idxs and (nr, nc) not in visited:
                cnt += dfs((nr, nc))
        return cnt
    return dfs(idxs[0]) == len(idxs)

def np_combination(mask):
    N = len(mask)
    i = N - 1
    while i > 0 and mask[i - 1] >= mask[i]:
        i -= 1
    if i == 0:
        return False
    j = N - 1
    while mask[i - 1] >= mask[j]:
        j -= 1
    mask[i - 1], mask[j] = mask[j], mask[i - 1]
    mask[i:] = sorted(mask[i:])
    return True

def solve():
    arr = [input().rstrip() for _ in range(5)]
    x = []
    for i in range(5):
        for j in range(5):
            if arr[i][j] == '*':
                x.append((i, j))
    ans = float("inf")
    mask = [0] * (25 - len(x)) + [1] * len(x)
    while 1:
        nxt_x = [divmod(i, 5) for i in range(25) if mask[i]]
        if is_connected(nxt_x):
            for p in permutations(nxt_x):
                total = sum([abs(x[i][0] - p[i][0]) + abs(x[i][1] - p[i][1]) for i in range(len(x))])
                if total < ans:
                    ans = total
        if not np_combination(mask):
            break
    print(ans)

solve()