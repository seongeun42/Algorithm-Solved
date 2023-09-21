import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] < 0:
        return n
    R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N, M, k = map(int, input().split())
    A = [0] + [*map(int, input().split())]
    R = [-1] * (N + 1)
    for _ in range(M):
        v, w = map(int, input().split())
        vr = find_root(v, R)
        wr = find_root(w, R)
        if vr != wr:
            if A[vr] < A[wr]:
                R[wr] = vr
            else:
                R[vr] = wr
    ans = 0
    for i in range(1, N + 1):
        if R[i] < 0:
            ans += A[i]
    print(ans if ans <= k else "Oh no")

solve()