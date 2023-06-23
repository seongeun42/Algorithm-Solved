import sys
input = sys.stdin.readline

def find_root(n):
    if R[n] != n:
        R[n] = find_root(R[n])
    return R[n]

N, M, K = map(int, input().split())
E = [[i + 1] + [*map(int, input().split())] for i in range(M)]
ans = [0] * K
for i in range(K):
    R = [i for i in range(N + 1)]
    w = 0
    for j in range(i, M):
        v, x, y = E[j]
        xr = find_root(x)
        yr = find_root(y)
        if xr != yr:
            w += v
            R[max(xr, yr)] = min(xr, yr)
    for j in range(1, N + 1):
        find_root(j)
    if len(set(R[1:])) != 1:
        break
    ans[i] = w
print(*ans)