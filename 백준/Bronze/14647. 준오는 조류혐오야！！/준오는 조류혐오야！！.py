n, m = map(int, input().split())
binggo = [[*input().rstrip().split()] for _ in range(n)]
cnt = [[0] * m for _ in range(n)]
total = 0
broke = 0
for i in range(n):
    for j in range(m):
        c = binggo[i][j].count('9')
        cnt[i][j] = c
        total += c
        if j == m - 1:
            hap = sum(cnt[i])
            if broke < hap:
                broke = hap
        if i == n - 1:
            hap = sum([cnt[v][j] for v in range(n)])
            if broke < hap:
                broke = hap
print(total - broke)