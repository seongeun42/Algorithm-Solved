from itertools import permutations
N, M = map(int, input().split())
nums = [*map(int, input().split())]
res = sorted(set(permutations(nums, M)))
for v in res:
    print(*v, sep=' ')