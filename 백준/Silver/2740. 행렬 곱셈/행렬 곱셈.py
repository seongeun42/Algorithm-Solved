import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(n)]
m, k = map(int, input().split())
B = [[*map(int, input().split())] for _ in range(m)]

ans = [[] for _ in range(n)]
for i in range(n):
    for j in range(k):
        ans[i].append(0)
        for l in range(m):
            ans[i][j] += A[i][l] * B[l][j]

for row in ans:
    print(*row, sep=" ")