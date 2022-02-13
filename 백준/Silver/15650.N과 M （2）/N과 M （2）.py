from itertools import combinations
N, M = map(int, input().split())
res = list(combinations(range(1, N + 1), M))
for v in res:
    print(*v, sep=' ')