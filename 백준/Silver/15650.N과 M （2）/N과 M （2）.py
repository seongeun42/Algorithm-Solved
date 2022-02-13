def backtrack(dep):
    if dep == M:
        print(*res[1:], sep=' ')
        return
    for i in range(res[dep] + 1, N + 1):
        if i not in res:
            res.append(i)
            backtrack(dep + 1)
            res.pop()

N, M = map(int, input().split())
res = [0]
backtrack(0)