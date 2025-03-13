import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_root(n, R, W):
    if R[n] != n:
        pre = R[n]
        R[n] = find_root(R[n], R, W)
        W[n] += W[pre]
    return R[n]

def solve():
    while 1:
        N, M = map(int, input().split())
        R = list(range(N + 1))
        W = [0] * (N + 1)
        if N == M == 0:
            break
        for _ in range(M):
            work = list(input().rstrip().split())
            a, b = map(int, work[1:3])
            ar = find_root(a, R, W)
            br = find_root(b, R, W)
            if work[0] == '!':
                rdiff = W[b] - W[a] - int(work[-1])
                if rdiff > 0:
                    R[ar] = R[br]
                    W[ar] = rdiff
                else:
                    R[br] = R[ar]
                    W[br] = -rdiff
            else:
                print("UNKNOWN" if ar != br else W[b] - W[a])

solve()