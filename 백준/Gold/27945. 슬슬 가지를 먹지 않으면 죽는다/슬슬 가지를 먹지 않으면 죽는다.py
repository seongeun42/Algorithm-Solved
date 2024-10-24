import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N, M = map(int, input().split())
    E = sorted([[*map(int, input().split())] for _ in range(M)], key=lambda x: x[2])
    R = [i for i in range(N + 1)]
    cnt = 0
    day = 0
    for u, v, t in E:
        if day + 1 != t:
            break
        ur = find_root(u, R)
        vr = find_root(v, R)
        if ur != vr:
            R[max(ur, vr)] = min(ur, vr)
            cnt += 1
            day = t
        if cnt == N - 1:
            break
    print(day + 1)

solve()