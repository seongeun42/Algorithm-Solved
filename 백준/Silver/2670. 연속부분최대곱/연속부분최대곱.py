import sys
input = sys.stdin.readline

N = int(input())
arr = [float(input()) for _ in range(N)]
dp = [arr[0]]
for i in range(1, N):
    dp.append(max(arr[i], dp[i - 1] * arr[i]))
print(f"{max(dp):.3f}")