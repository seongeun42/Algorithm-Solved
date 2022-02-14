from itertools import product
N, M = map(int, input().split())
res = list(product(range(1, N+1), repeat=M))
for v in res:
    print(*v, sep=' ')