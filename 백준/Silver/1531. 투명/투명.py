import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    pic = [[0] * 100 for _ in range(100)]
    for _ in range(N):
        lr, lc, rr, rc = map(int, input().split())
        for i in range(lr, rr + 1):
            for j in range(lc, rc + 1):
                pic[i - 1][j - 1] += 1
    ans = 0
    for i in range(100):
        for j in range(100):
            if pic[i][j] > M:
                ans += 1
    print(ans)

solve()