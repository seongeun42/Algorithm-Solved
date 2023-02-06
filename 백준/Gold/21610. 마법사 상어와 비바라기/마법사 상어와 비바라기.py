def waterCopy(r, c):
    ddc = [-1, 1, 1, -1]
    ddr = [-1, -1, 1, 1]
    addWater = 0
    for i in range(4):
        if 0 <= r + ddr[i] < N and 0 <= c + ddc[i] < N:
            if pan[r + ddr[i]][c + ddc[i]] != 0:
                addWater += 1
    return addWater

def cludeMake(dep):
    c = []
    for i in range(N):
        for j in range(N):
            if visit[i][j] != dep and pan[i][j] >= 2:
                c.append([i, j])
                pan[i][j] -= 2
    return c

N, M = map(int, input().split())
pan = [[*map(int, input().split())] for _ in range(N)]
clude = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]
visit = [[-1] * N for _ in range(N)]
# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dc = [-1, -1, 0, 1, 1, 1, 0, -1]
dr = [0, -1, -1, -1, 0, 1, 1, 1]
for dep in range(M):
    d, r = map(int, input().split())
    for i in range(len(clude)):
        mr = (clude[i][0] + (dr[d - 1] * r)) % N
        mr = mr + N if mr < 0 else mr
        mc = (clude[i][1] + (dc[d - 1] * r)) % N
        mc = mc + N if mc < 0 else mc
        clude[i] = [mr, mc]
        pan[mr][mc] += 1
        visit[mr][mc] = dep
    for cr, cc in clude:
        pan[cr][cc] += waterCopy(cr, cc)
    clude = cludeMake(dep)
print(sum(map(sum, pan)))