from itertools import combinations
N = int(input())
abil = [[*map(int, input().split())] for _ in range(N)]
res = 1e9
for S in combinations(range(N), N//2):
    L = set(range(N)) - set(S)
    start, link = 0, 0
    for i in S:
        for j in S:
            start += abil[i][j]
    for i in L:
        for j in L:
            link += abil[i][j]
    res = min(res, abs(start - link))
print(res)