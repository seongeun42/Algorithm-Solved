import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    ans = 0
    s, e = map(int, input().split())
    for _ in range(N - 1):
        x, y = map(int, input().split())
        if e < x:
            ans += e - s
            s = x
        if e < y:
            e = y
    ans += e - s
    print(ans)

solve()