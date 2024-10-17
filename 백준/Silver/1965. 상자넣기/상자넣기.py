def solve():
    n = int(input())
    box = [*map(int, input().split())]
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if box[j] < box[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
    print(max(dp))

solve()