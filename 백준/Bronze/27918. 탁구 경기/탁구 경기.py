n = int(input())
v = [input() for _ in range(n)]
d, p = 0, 0
for c in v:
    if c == 'D':
        d += 1
    else:
        p += 1
    if abs(d - p) > 1:
        break
print(d, ':', p, sep='')