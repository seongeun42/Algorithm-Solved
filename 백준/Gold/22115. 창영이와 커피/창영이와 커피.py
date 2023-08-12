def solve():
    N, K = map(int, input().split())
    C = [*map(int, input().split())]
    dp = [0] + [101] * K
    for c in C:
        for k in range(K, c - 1, -1):
            if dp[k] > dp[k - c]:
                dp[k] = dp[k - c] + 1
    print(-1 if dp[K] == 101 else dp[K])

solve()