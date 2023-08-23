import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    nums = [*map(int, input().split())]
    dp = [[0] * N for _ in range(N)]
    for l in range(N):
        for s in range(N - l):
            e = s + l
            if s == e:
                dp[s][e] = 1
            elif nums[s] == nums[e]:
                if e - s + 1 == 2:
                    dp[s][e] = 1
                else:
                    dp[s][e] = dp[s + 1][e - 1]

    M = int(input())
    for _ in range(M):
        S, E = map(int, input().split())
        print(dp[S - 1][E - 1])

solve()