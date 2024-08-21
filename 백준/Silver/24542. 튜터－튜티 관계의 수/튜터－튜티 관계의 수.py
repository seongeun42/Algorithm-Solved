import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] < 0:
        return n
    R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N, M = map(int, input().split())
    R = [-1] * (N + 1)
    for _ in range(M):
        u, v = map(int, input().split())
        ur = find_root(u, R)
        vr = find_root(v, R)
        if ur != vr:
            if R[ur] <= R[vr]:
                R[ur] += R[vr]
                R[vr] = ur
            else:
                R[vr] += R[ur]
                R[ur] = vr
    ans = 1
    for i in range(1, N + 1):
        if R[i] < 0:
            ans *= -R[i]
    print(ans % 1000000007)

solve()