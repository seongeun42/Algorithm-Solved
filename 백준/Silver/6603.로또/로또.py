from itertools import combinations
while 1:
    ks = [*map(int, input().split())]
    if len(ks) == 1 and not ks[0]:
        break
    res = list(combinations(ks[1:], 6))
    for v in res:
        print(*v, sep=' ')
    print()