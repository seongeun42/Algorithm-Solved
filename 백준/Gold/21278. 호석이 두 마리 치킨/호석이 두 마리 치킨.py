import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[100] * N for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A - 1][B - 1] = 1
    G[B - 1][A - 1] = 1

for m in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                G[i][j] = 0
            elif G[i][j] > G[i][m] + G[m][j]:
                G[i][j] = G[i][m] + G[m][j]

c1, c2, t = -1, -1, 1e9
for i in range(N):
    for j in range(i + 1, N):
        tmp = 0
        for k in range(N):
            if k != i and k != j:
                tmp += min(G[i][k], G[j][k])
        if t > tmp:
            c1, c2, t = i, j, tmp

print(c1 + 1, c2 + 1, t * 2)