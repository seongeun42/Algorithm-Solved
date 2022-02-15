def backtrack(dep):
    if dep == M:
        print(*res, sep=' ')
    else:
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue
            res.append(v)
            backtrack(dep + 1)
            res.pop()

N, M = map(int, input().split())
nums = sorted([*map(int, input().split())])
res = []
backtrack(0)