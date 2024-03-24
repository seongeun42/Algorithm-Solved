import sys
input = sys.stdin.readline

def find_root(n):
    if R[n] != n:
        R[n] = find_root(R[n])
    return R[n]

N, M = map(int, input().split())
R = [i for i in range(N + 1)]
cnt = 0
for _ in range(M):
    u, v = map(int, input().split())
    ur = find_root(u)
    vr = find_root(v)
    if ur != vr:
        R[max(ur, vr)] = min(ur, vr)
    else:
        cnt += 1
for i in range(1, N + 1):
    if R[i] == i:
        cnt += 1
print(cnt - 1)