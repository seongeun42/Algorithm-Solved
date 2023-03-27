n = int(input())
p = [[0] * 1001 for _ in range(1001)]
a = [0] * (n + 1)
for pn in range(n):
    lc, lr, w, h = map(int, input().split())
    for i in range(lr, lr + h):
        for j in range(lc, lc + w):
            p[i][j] = pn + 1

for i in range(1001):
    for j in range(1001):
        a[p[i][j]] += 1

print(*a[1::], sep="\n")