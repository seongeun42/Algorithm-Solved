import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] < 0:
        return n
    R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N = int(input())
    R = [-1] * (N + 1)
    for _ in range(N - 2):
        v, w = map(int, input().split())
        vr = find_root(v, R)
        wr = find_root(w, R)
        if vr != wr:
            R[max(vr, wr)] = min(vr, wr)
    root = []
    for i in range(1, N + 1):
        if R[i] < 0:
            root.append(i)
    print(*root)

solve()