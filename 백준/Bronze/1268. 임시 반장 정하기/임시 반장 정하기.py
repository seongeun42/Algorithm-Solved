n = int(input())
c = [[*map(int, input().split())] for _ in range(n)]
chk = [[0] * n for _ in range(n)]
for i in range(5):
    for j in range(n):
        for l in range(j + 1, n):
            if c[j][i] == c[l][i]:
                chk[j][l], chk[l][j] = 1, 1
ans = 0
for i in range(1, n):
    if sum(chk[ans]) < sum(chk[i]):
        ans = i
print(ans + 1)