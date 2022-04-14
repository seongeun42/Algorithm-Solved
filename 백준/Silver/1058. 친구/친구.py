import sys
input = sys.stdin.readline

N = int(input())
F = [input().strip() for _ in range(N)]
visit = [[0] * N for _ in range(N)]

for m in range(N):
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if F[i][j] == 'Y' or (F[i][m] == 'Y' and F[m][j] == 'Y'):
                visit[i][j] = 1

print(max(map(sum, visit)))