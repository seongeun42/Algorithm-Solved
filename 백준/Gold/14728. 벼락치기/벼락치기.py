import sys
input = sys.stdin.readline

N, T = map(int, input().split())
times, scores = [0], [0]
for _ in range(N):
    t, s = map(int, input().split())
    times.append(t)
    scores.append(s)
dp = [[0] * (T + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, T + 1):
        if j >= times[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-times[i]] + scores[i])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][T])