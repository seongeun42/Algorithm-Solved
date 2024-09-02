import sys
input = sys.stdin.readline

def solve():
    M, N = map(int, input().split())
    K = int(input())
    jido = [input().rstrip() for _ in range(M)]
    pre_sum = [[[0] * 3 for _ in range(N + 1)] for _ in range(M + 1)]
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if jido[i - 1][j - 1] == 'J':
                pre_sum[i][j] = [1, 0, 0]
            elif jido[i - 1][j - 1] == 'O':
                pre_sum[i][j] = [0, 1, 0]
            elif jido[i - 1][j - 1] == 'I':
                pre_sum[i][j] = [0, 0, 1]
            for r in range(3):
                pre_sum[i][j][r] += pre_sum[i - 1][j][r] + pre_sum[i][j - 1][r] - pre_sum[i - 1][j - 1][r]
    for _ in range(K):
        a, b, c, d = map(int, input().split())
        for i in range(3):
            print(pre_sum[c][d][i] - pre_sum[c][b - 1][i] - pre_sum[a - 1][d][i] + pre_sum[a - 1][b - 1][i], end=' ')
        print()

solve()