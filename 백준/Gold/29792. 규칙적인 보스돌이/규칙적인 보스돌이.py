import sys, math
input = sys.stdin.readline

def solve():
    N, M, K = map(int, input().split())
    damage = [int(input()) for _ in range(N)]
    boss = [[*map(int, input().split())] for _ in range(K)]
    ans = []
    for d in damage:
        dp = [0] * 901
        max_v = 0
        for hp, meso in boss:
            need = math.ceil(hp/d)
            if 900 < need:
                continue
            for t in range(900, need - 1, -1):
                if dp[t] < meso + dp[t - need]:
                    dp[t] = meso + dp[t - need]
            max_v = max(dp)
        ans.append(max_v)
    print(sum(sorted(ans, reverse=True)[:M]))

solve()