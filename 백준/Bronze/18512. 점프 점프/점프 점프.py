x, y, p1, p2 = map(int, input().split())
for i in range(200):
    if p1 == p2:
        print(p1)
        break
    if p1 < p2:
        p1 += x
    else:
        p2 += y
else:
    print(-1)