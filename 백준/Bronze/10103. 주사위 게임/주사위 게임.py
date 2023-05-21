n = int(input())
c, s = 100, 100
for _ in range(n):
    sc, ss = map(int, input().split())
    if sc == ss:
        continue
    if sc > ss:
        s -= sc
    else:
        c -= ss
print(c)
print(s)