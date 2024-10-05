import sys
input = sys.stdin.readline

def solve():
    R, C, Q = map(int, input().split())
    picture = [[*map(int, input().split())] for _ in range(R)]
    prefix = [[0] * (C + 1) for _ in range(R + 1)]
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            prefix[i][j] = picture[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]
    for _ in range(Q):
        r1, c1, r2, c2 = map(int, input().split())
        cnt = (r2 - r1 + 1) * (c2 - c1 + 1)
        hap = prefix[r2][c2] - prefix[r1 - 1][c2] - prefix[r2][c1 - 1] + prefix[r1 - 1][c1 - 1]
        print(hap // cnt)

solve()