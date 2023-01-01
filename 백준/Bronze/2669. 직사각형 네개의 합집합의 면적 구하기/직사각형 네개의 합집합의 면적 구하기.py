g = [[0] * 101 for _ in range(101)]
for _ in range(4):
    ldx, ldy, rux, ruy = map(int, input().split())
    for i in range(ldy, ruy):
        for j in range(ldx, rux):
            g[i][j] = 1
print(sum(map(sum, g)))