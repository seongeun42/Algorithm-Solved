from itertools import combinations
N, M = map(int, input().split())
nums = sorted([*map(int, input().split())])
res = sorted(set(combinations(nums, M)))
for v in res:
    print(*v, sep=' ')