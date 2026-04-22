import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N, Q = map(int, input().split())
    size = [0] + [*map(int, input().split())]
    R = list(range(N + 1))
    power = [0] * (N + 1)
    for _ in range(Q):
        a, b = map(int, input().split())
        ar = find_root(a, R)
        br = find_root(b, R)
        if ar != br:
            min_r, max_r = min(ar, br), max(ar, br)
            R[max_r] = min_r
            power[min_r] += power[max_r] + size[min_r] * size[max_r]
            size[min_r] += size[max_r]
            print(power[min_r])
        else:
            print(power[ar])

solve()