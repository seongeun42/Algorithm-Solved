def backtrack(dep):
    if dep == 6:
        print(*res, sep=' ')
    else:
        for v in S:
            if res and v < res[-1]:
                continue
            if v not in res:
                res.append(v)
                backtrack(dep + 1)
                res.pop()

while 1:
    ks = [*map(int, input().split())]
    S = sorted(ks[1:])
    if len(ks) == 1 and not ks[0]:
        break
    res = []
    backtrack(0)
    print()