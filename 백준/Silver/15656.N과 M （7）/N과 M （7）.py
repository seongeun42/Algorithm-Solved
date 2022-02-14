from itertools import product
N, M = map(int, input().split())
nums = sorted([*map(int, input().split())])
res = list(product(nums, repeat=M))
for v in res:
    print(*v, sep=' ')