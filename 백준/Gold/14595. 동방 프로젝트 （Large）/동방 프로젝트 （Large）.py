import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    M = int(input())
    if M == 0:
        print(N)
        return
    broke = sorted([[*map(int, input().split())] for _ in range(M)])
    s, e = 1, 1 if broke[0][0] > 1 else broke[0][1]
    ans = 1
    for x, y in broke:
        if e < x:
            ans += x - e
            s, e = x, y
        elif s <= x <= e and e < y:
            e = y
    if e < N:
        ans += N - e
    print(ans)

solve()