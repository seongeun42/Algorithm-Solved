def solve():
    G = int(input())
    ans = []
    s, e = 1, 2
    while 1:
        if (s + 1) ** 2 - s ** 2 > G:
            break
        v = e ** 2 - s ** 2
        if v == G:
            ans.append(e)
        elif v < G:
            e += 1
            continue
        s += 1
    if len(ans) == 0:
        print(-1)
    else:
        print(*ans, sep="\n")

solve()