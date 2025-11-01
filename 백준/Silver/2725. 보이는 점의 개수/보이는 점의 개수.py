import sys, math
input = sys.stdin.readline

prefix = [[0] * 1001 for _ in range(1001)]
for i in range(1001):
    for j in range(1001):
        if i == j == 0:
            continue
        elif i == 0 or j == 0:
            prefix[i][j] = 1
        else:
            see = 1 if math.gcd(i, j) == 1 else 0
            prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + see

C = int(input())
for _ in range(C):
    N = int(input())
    print(prefix[N][N])