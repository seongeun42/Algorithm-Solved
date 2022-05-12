import sys
input = sys.stdin.readline

N, M = map(int, input().split())
res = [['-'] * N for _ in range(N)]
G = [[1e9] * N for _ in range(N)]
for _ in range(M):
    A, B, Time = map(int, input().split())
    if Time < G[A - 1][B - 1]:
        G[A - 1][B - 1] = Time
        G[B - 1][A - 1] = Time
        res[A - 1][B - 1] = [A, B]
        res[B - 1][A - 1] = [B, A]
        
for m in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                res[i][j] = '-'
            elif G[i][j] > G[i][m] + G[m][j]:
                G[i][j] = G[i][m] + G[m][j]
                res[i][j] = res[i][m] + res[m][j][1:]
                
for i in range(N):
    for j in range(N):
        print('-' if i == j else res[i][j][1], end=' ')
    print()