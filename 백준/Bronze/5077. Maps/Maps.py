import sys
input = sys.stdin.readline

def is_matched(sr, sc):
    for i in range(r):
        for j in range(c):
            if pic[i][j] != snow[sr + i][sc + j]:
                return 0
    return 1

T = int(input())
for _ in range(T):
    r, c = map(int, input().split())
    pic = [input().rstrip() for _ in range(r)]
    y, x = map(int, input().split())
    snow = [input().rstrip() for _ in range(y)]
    ans = 0
    for i in range(y - r + 1):
        for j in range(x - c + 1):
            ans += is_matched(i, j)
    print(ans)