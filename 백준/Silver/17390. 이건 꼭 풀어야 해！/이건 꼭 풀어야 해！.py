import sys
input = sys.stdin.readline

def solve():
    N, Q = map(int, input().split())
    B = sorted([*map(int, input().split())])
    prefixed = [0]
    for i in range(N):
        prefixed.append(B[i] + prefixed[i])
    for _ in range(Q):
        L, R = map(int, input().split())
        print(prefixed[R] - prefixed[L - 1])

solve()