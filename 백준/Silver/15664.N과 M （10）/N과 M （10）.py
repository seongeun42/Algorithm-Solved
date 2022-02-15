def backtrack(dep):
    if dep == M:
        print(*res, sep=' ')
    else:
        cur = -1
        for i, v in enumerate(nums):
            if res and v < res[-1]:
                continue
            if not used[i] and v != cur:
                cur = v
                res.append(v)
                used[i] = 1
                backtrack(dep + 1)
                res.pop()
                used[i] = 0

N, M = map(int, input().split())
nums = sorted([*map(int, input().split())])
res = []
used = [0] * N
backtrack(0)