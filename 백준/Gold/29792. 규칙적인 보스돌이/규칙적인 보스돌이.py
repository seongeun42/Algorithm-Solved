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
            for t in range(900, 0, -1):
                if d * t >= hp:
                    if dp[t] < meso + dp[t - need]:
                        dp[t] = meso + dp[t - need]
                        if dp[t] > max_v:
                            max_v = dp[t]
        ans.append(max_v)
    print(sum(sorted(ans, reverse=True)[:M]))

solve()