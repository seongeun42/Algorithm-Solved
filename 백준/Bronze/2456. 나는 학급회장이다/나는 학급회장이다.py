n = int(input())
s = [0] * 3
ss = [0] * 3
for _ in range(n):
    c = [*map(int, input().split())]
    for i in range(3):
        s[i] += c[i]
        ss[i] += c[i] ** 2

if s.count(max(s)) == 1:
    print(s.index(max(s)) + 1, max(s))
else:
    idx = ss.index(max(ss))
    print(idx + 1 if ss.count(max(ss)) == 1 else 0, s[idx])