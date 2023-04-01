n = int(input())
scores = [[*map(int, input().split())] for _ in range(n)]
s = [[0] * 101 for _ in range(3)]
ans = [0] * n
for i in range(n):
    for j in range(3):
        s[j][scores[i][j]] += 1
for i in range(n):
    for j in range(3):
        if s[j][scores[i][j]] == 1:
            ans[i] += scores[i][j]
print(*ans, sep="\n")