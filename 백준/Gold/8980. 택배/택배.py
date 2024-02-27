import sys
input = sys.stdin.readline

def solve():
    N, C = map(int, input().split())
    M = int(input())
    info = sorted([[*map(int, input().split())] for _ in range(M)], key=lambda x: x[1])
    truck = [0] * (N + 1)
    ans = 0
    for u, v, w in info:
        predict_w = w
        for i in range(u, v):
            predict_w = min(C - truck[i], predict_w)
        for i in range(u, v):
            truck[i] += predict_w
        ans += predict_w
    print(ans)

solve()