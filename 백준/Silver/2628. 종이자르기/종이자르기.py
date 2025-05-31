garo, sero = map(int, input().split())
cut = int(input())
g, s = [0, garo], [0, sero]
for _ in range(cut):
    d, n = map(int, input().split())
    if d == 0:
        s.append(n)
    else:
        g.append(n)
g.sort()
s.sort()
glen = [g[i] - g[i - 1] for i in range(len(g))]
slen = [s[i] - s[i - 1] for i in range(len(s))]
print(max(glen) * max(slen))