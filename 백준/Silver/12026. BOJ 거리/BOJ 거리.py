N = int(input())
S = input()
prev = {'B': 'J', 'O': 'B', 'J': 'O'}
dp = [1e9] * N
dp[0] = 0
for i in range(1, N):
    for j in range(1, i + 1):
        if prev[S[i]] == S[i - j]:
            v = dp[i - j] + j * j
            if v < dp[i]:
                dp[i] = v
print(dp[-1] if dp[-1] != 1e9 else -1)