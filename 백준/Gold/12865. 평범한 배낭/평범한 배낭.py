import sys
input = sys.stdin.readline
N, K = map(int, input().split())
dp = [0] * (K + 1)
for i in range(1, N + 1):
    w, v = map(int, input().split())
    for bw in range(K, 0, -1):
        if bw >= w:
            dp[bw] = max(dp[bw], v + dp[bw - w])
print(dp[K])