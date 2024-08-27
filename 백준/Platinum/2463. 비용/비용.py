import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] < 0:
        return n
    R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N, M = map(int, input().split())
    edge = []
    remain = 0
    for _ in range(M):
        x, y, w = map(int, input().split())
        remain += w
        edge.append((w, x, y))
    edge.sort(reverse=True)
    R = [-1] * (N + 1)
    ans = 0
    for w, u, v in edge:
        ur = find_root(u, R)
        vr = find_root(v, R)
        if ur != vr:
            ans += (R[ur] * R[vr] * remain) % 1000000000
            if ur < vr:
                R[ur] += R[vr]
                R[vr] = ur
            elif ur > vr:
                R[vr] += R[ur]
                R[ur] = vr
        remain -= w
    print(ans % 1000000000)

solve()