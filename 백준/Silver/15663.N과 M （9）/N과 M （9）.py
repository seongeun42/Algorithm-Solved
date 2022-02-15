from itertools import permutations
N, M = map(int, input().split())
nums = sorted([*map(int, input().split())])
res = sorted(list(set(permutations(nums, M))))
for v in res:
    print(*v, sep=' ')