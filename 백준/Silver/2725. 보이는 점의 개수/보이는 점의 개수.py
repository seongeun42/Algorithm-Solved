import sys, math
input = sys.stdin.readline

def solve():
    C = int(input())
    Q = [int(input()) for _ in range(C)]
    max_q = max(Q) + 1
    prefix = [[0] * max_q for _ in range(max_q)]
    for i in range(max_q):
        for j in range(max_q):
            if i == j == 0:
                continue
            elif i == 0 or j == 0:
                prefix[i][j] = 1
            else:
                see = 1 if math.gcd(i, j) == 1 else 0
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + see
    for q in Q:
        print(prefix[q][q])

solve()