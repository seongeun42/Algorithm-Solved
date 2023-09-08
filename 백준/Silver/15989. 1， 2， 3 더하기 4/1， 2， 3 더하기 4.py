import sys
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    dp = [1] * 10001
    for i in range(2, 10001):
        dp[i] += dp[i - 2]
    for i in range(3, 10001):
        dp[i] += dp[i - 3]
    for _ in range(T):
        print(dp[int(input())])