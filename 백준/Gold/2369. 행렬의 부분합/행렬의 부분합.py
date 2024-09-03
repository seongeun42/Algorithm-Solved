from collections import defaultdict
import sys
input = sys.stdin.readline

def solve():
    N, M, K = map(int, input().split())
    matr = [[*map(int, input().split())] for _ in range(N)]
    pre_sum = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            pre_sum[i][j] = matr[i - 1][j - 1] + pre_sum[i - 1][j] + pre_sum[i][j - 1] - pre_sum[i - 1][j - 1]
    ans = 0
    for i in range(1, N + 1):
        for j in range(i, N  + 1):
            remain = defaultdict(int)
            for w in range(1, M + 1):
                hap = pre_sum[j][w] - pre_sum[i - 1][w]
                remain[hap % K] += 1
            ans += remain[0]
            for v in remain.values():
                ans += v * (v - 1) // 2
    print(ans)

solve()