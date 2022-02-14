from itertools import combinations_with_replacement
N, M = map(int, input().split())
res = list(combinations_with_replacement(range(1, N+1), M))
for v in res:
    print(*v, sep=' ')