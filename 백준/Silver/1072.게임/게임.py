x, y = map(int, input().split())
z = (y * 100) // x
if z >= 99: print(-1)
else:
    s, e = 0, 10**9
    while s <= e:
        m = (s + e) // 2
        v = ((y + m) * 100) // (x + m)
        if v > z:
            e = m - 1
        else:
            s = m + 1
    print(e + 1)