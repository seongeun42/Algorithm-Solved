def backtrack(dep):
    if dep == M:
        print(*res, sep=' ')
        return
    for i in range(1, N + 1):
        f = 0
        for j in range(dep):
            if res[j] == i:
                f = 1
                break
        if not f:
            res[dep] = i
            backtrack(dep + 1)

N, M = map(int, input().split())
res = [0] * M
for i in range(1, N + 1):
    res[0] = i
    backtrack(1)