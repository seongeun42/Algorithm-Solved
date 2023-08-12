def solve():
    G = int(input())
    ans = []
    s, e = 1, 2
    while 1:
        if s * 2 >= G:
            break
        v = (e + s) * (e - s)
        if v == G:
            ans.append(e)
        elif v < G:
            e += 1
            continue
        s += 1
    if len(ans):
        print(*ans, sep="\n")
    else:
        print(-1)

solve()