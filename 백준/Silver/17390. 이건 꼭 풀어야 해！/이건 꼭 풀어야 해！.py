import sys
input = sys.stdin.readline

def solve():
    N, Q = map(int, input().split())
    B = sorted([*map(int, input().split())])
    prefixed = B[:]
    for i in range(1, N):
        prefixed[i] += prefixed[i - 1]
    for _ in range(Q):
        L, R = map(int, input().split())
        print(prefixed[R - 1] - prefixed[L - 1] + B[L - 1])

solve()