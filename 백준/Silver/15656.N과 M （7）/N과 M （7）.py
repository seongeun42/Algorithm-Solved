def backtrack(dep):
    if dep == M:
        print(*res, sep=' ')
    else:
        for v in nums:
            res.append(v)
            backtrack(dep + 1)
            res.pop()

N, M = map(int, input().split())
nums = sorted([*map(int, input().split())])
res = []
backtrack(0)