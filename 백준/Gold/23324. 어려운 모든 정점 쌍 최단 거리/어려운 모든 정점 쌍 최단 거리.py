import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] < 0:
        return n
    R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N, M, K = map(int, input().split())
    R = [-1] * (N + 1)
    for i in range(M):
        u, v = map(int, input().split())
        if i == K - 1:
            continue
        ur = find_root(u, R)
        vr = find_root(v, R)
        if ur < vr:
            R[ur] += R[vr]
            R[vr] = ur
        elif ur > vr:
            R[vr] += R[ur]
            R[ur] = vr
    ans = 1
    cnt = 0
    for i in range(1, N + 1):
        if R[i] < 0:
            ans *= -R[i]
            cnt += 1
    print(ans if cnt != 1 else 0)

solve()