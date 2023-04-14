import sys
input = sys.stdin.readline

n, m = map(int, input().split())
G = [[*map(int, input().split())] for _ in range(n)]

for mid in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and G[i][j] > G[i][mid] + G[mid][j]:
                G[i][j] = G[i][mid] + G[mid][j]

for _ in range(m):
    a, b, c = map(int, input().split())
    print("Enjoy other party" if G[a - 1][b - 1] <= c else "Stay here")