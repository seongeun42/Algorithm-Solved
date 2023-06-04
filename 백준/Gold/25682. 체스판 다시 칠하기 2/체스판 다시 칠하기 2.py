import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
B = [input().strip() for _ in range(N)]
sb = [[0] * (M + 1) for _ in range(N + 1)]
sw = [[0] * (M + 1) for _ in range(N + 1)]
ans = N * M
for i in range(1, N + 1):
    mb = 'W' if i % 2 else 'B'
    mw = 'B' if i % 2 else 'W'
    for j in range(1, M + 1):
        sb[i][j] = sb[i - 1][j] + sb[i][j - 1] - sb[i - 1][j - 1]
        sw[i][j] = sw[i - 1][j] + sw[i][j - 1] - sw[i - 1][j - 1]
        if B[i - 1][j - 1] != mb:
            sb[i][j] += 1
        if B[i - 1][j - 1] != mw:
            sw[i][j] += 1
        if i >= K and j >= K:
            cntb = sb[i][j] - sb[i - K][j] - sb[i][j - K] + sb[i - K][j - K]
            cntw = sw[i][j] - sw[i - K][j] - sw[i][j - K] + sw[i - K][j - K]
            ans = min(ans, cntb, cntw)
        mb, mw = mw, mb
print(ans)