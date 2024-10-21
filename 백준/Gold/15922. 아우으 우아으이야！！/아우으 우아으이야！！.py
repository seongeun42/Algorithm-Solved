import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    coordi = sorted([[*map(int, input().split())] for _ in range(N)])
    ans = 0
    s, e = coordi[0]
    for x, y in coordi[1:]:
        if e < x:
            ans += e - s
            s, e = x, y
        elif e >= x and e < y:
            e = y
    ans += e - s
    print(ans)

solve()