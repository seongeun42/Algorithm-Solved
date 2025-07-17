import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    A, B = map(int, input().split())
    C = int(input())
    topping = sorted([int(input()) for _ in range(N)], reverse=True)
    total, price = C, A
    ans = total / price
    for t in topping:
        total += t
        price += B
        cal = total / price
        if ans < cal:
            ans = cal
    print(int(ans))

solve()