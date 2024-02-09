import sys
input = sys.stdin.readline

def find_root(R, n):
    if R[n] < 0:
        return n
    R[n] = find_root(R, R[n])
    return R[n]

def solve():
    N, M = map(int, input().split())
    R = [-1] * (N + 1)
    for _ in range(M):
        X, Y = map(int, input().split())
        xr = find_root(R, X)
        yr = find_root(R, Y)
        if xr != yr:
            if xr < yr:
                R[xr] += R[yr]
                R[yr] = xr
            else:
                R[yr] += R[xr]
                R[xr] = yr
    C, H, K = map(int, input().split())
    cr = find_root(R, C)
    hr = find_root(R, H)
    not_yet = []
    for i in range(1, N + 1):
        # 루트의 값이 음수이고, 루트가 C와 H와 다르다면 아직 동맹 X
        if R[i] < 0 and i != cr and i != hr:
            not_yet.append(R[i])
    not_yet.sort()
    return -(R[cr] + sum(not_yet[:K]))

print(solve())