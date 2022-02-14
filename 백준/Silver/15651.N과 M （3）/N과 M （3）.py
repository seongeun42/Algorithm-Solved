def backtrack(dep):
    if dep == M:
        print(*res, sep=' ')
    else:
        for i in range(1, N+1):
            res.append(i)
            backtrack(dep + 1)
            res.pop()

N, M = map(int, input().split())
res = []
backtrack(0)