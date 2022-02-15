from itertools import product
N, M = map(int, input().split())
nums = [*map(int, input().split())]
res = sorted(set(product(nums, repeat=M)))
for v in res:
    print(*v, sep=' ')