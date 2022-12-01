import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ice = [[1] * n for _ in range(n)]
for _ in range(m):
    no1, no2 = map(int, input().split())
    ice[no1 - 1][no2 - 1], ice[no2 - 1][no1 - 1] = 0, 0

res = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if ice[i][j] and ice[i][k] and ice[j][k]:
                res += 1
print(res)