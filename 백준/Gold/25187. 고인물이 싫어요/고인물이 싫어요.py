import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] < 0:
        return n
    R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N, M, Q = map(int, input().split())
    water = [-1] + [*map(int, input().split())]
    R = [-1] * (N + 1)
    for _ in range(M):
        u, v = map(int, input().split())
        ur = find_root(u, R)
        vr = find_root(v, R)
        if ur < vr:
            water[ur] += water[vr]
            R[ur] += R[vr]
            R[vr] = ur
        elif ur > vr:
            water[vr] += water[ur]
            R[vr] += R[ur]
            R[ur] = vr
    for _ in range(Q):
        K = int(input())
        kr = find_root(K, R)
        print(1 if -R[kr] // 2 < water[kr] else 0)

solve()