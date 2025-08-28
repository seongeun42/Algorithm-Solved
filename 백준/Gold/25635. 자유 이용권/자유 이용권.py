import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    a = sorted([*map(int, input().split())])
    ans = sum(a[:-1])
    ans += min(ans + 1, a[-1])
    print(ans)

solve()