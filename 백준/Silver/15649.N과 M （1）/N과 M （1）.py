from itertools import permutations
N, M = map(int, input().split())
res = list(permutations(range(1, N + 1), M))
for v in res:
    print(*v, sep=' ')