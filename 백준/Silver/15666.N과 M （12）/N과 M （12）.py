from itertools import combinations_with_replacement
N, M = map(int, input().split())
nums = sorted([*map(int, input().split())])
res = sorted(set(combinations_with_replacement(nums, M)))
for v in res:
    print(*v, sep=' ')