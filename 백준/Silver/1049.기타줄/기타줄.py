n, m = map(int, input().split())
p, s = [0] * m, [0] * m
for i in range(m):
    p[i], s[i] = map(int, input().split())
six = min(p)
one = min(s)
d, m = divmod(n, 6)
a = d + 1 if m else d
print(min(one * n, six * d + one * m, six * a))