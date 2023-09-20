import sys, heapq
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N = int(input())
    E = []
    for i in range(N):
        E.append((N, i, int(input())))
    for i in range(N):
        l = [*map(int, input().split())]
        for j in range(N):
            if i == j: continue
            E.append((i, j, l[j]))
    E.sort(key=lambda x: x[2])
    R = [i for i in range(N + 1)]
    res = 0
    cnt = 0
    for s, e, c in E:
        sr = find_root(s, R)
        er = find_root(e, R)
        if sr != er:
            cnt += 1
            res += c
            R[max(sr, er)] = R[min(sr, er)]
        if cnt == N:
            break
    print(res)

solve()