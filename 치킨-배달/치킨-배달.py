from itertools import combinations
n, m = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(n)]
home = []
chik = []
for i in range(n):
    for j in range(n):
        if jido[i][j] == 1:
            home.append([i, j])
        elif jido[i][j] == 2:
            chik.append([i, j])
res = float('inf')
for slt in combinations(chik, m):
    total = 0
    for h in home:
        total += min([abs(h[0] - c[0]) + abs(h[1] - c[1]) for c in slt])
        if res <= total: break
    res = min(res, total)
print(res)