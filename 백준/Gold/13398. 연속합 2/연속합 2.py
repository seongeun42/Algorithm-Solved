import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    if n == 1:
        print(arr[0])
        return
    dp = [[arr[0], 0]]
    ans = -1e9
    for i in range(1, n):
        dp.append([max(dp[i - 1][0] + arr[i], arr[i]), max(dp[i - 1][1] + arr[i], dp[i - 1][0])])
        max_v = max(dp[i])
        if ans < max_v:
            ans = max_v
    print(ans)

solve()