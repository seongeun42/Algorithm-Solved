import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N, M = map(int, input().split())
    R = list(range(N + 1))
    cnt = N
    for _ in range(M):
        a, b = map(int, input().split())
        ar = find_root(a, R)
        br = find_root(b, R)
        if ar != br:
            R[max(ar, br)] = min(ar, br)
            cnt -= 1
    print(cnt - 1)

solve()