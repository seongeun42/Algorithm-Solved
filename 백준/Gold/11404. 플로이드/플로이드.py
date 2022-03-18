n = int(input())
m = int(input())
G = [[1e9] * n for _ in range(n)]
for _ in range(m):
    sc, ec, c = map(int, input().split())
    G[sc - 1][ec - 1] = min(c, G[sc - 1][ec - 1])

for mid in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and G[i][j] > G[i][mid] + G[mid][j]:
                G[i][j] = G[i][mid] + G[mid][j]
for arr in G:
    for v in arr:
        print(v if v != 1e9 else 0, end=' ')
    print()