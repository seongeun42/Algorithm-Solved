import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    P = sorted([int(input()) for _ in range(M)])
    price, total = 0, 0
    for i in range(M):
        new_total = P[i] * min(N, M - i)
        if new_total > total:
            price, total = P[i], new_total
    print(price, total)

solve()