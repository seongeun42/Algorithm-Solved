import sys
input = sys.stdin.readline

def find_root(n):
    if R[n] != n:
        R[n] = find_root(R[n])
    return R[n]

N, M = map(int, input().split())
R = [i for i in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    ur = find_root(u)
    vr = find_root(v)
    if ur != vr:
        R[max(ur, vr)] = min(ur, vr)
for i in range(1, N + 1):
    find_root(i)
lect = [*map(int, input().split())]
ans = 0
cur = R[lect[0]]
for i in range(1, N):
    if cur != R[lect[i]]:
        ans += 1
        cur = R[lect[i]]
print(ans)