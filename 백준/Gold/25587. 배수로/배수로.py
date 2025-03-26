import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_root(n, R):
    if R[n] < 0:
        return n
    R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N, M = map(int, input().split())
    A = [0] + [*map(int, input().split())]
    B = [0] + [*map(int, input().split())]
    R = [-1] * (N + 1)
    cnt = 0
    for i in range(1, N + 1):
        if A[i] < B[i]:
            cnt += 1
    for _ in range(M):
        query = input().rstrip()
        if query[0] == '2':
            print(cnt)
        else:
            _, x, y = map(int, query.split())
            xr = find_root(x, R)
            yr = find_root(y, R)
            if xr != yr:
                if A[xr] < B[xr]:
                    cnt += R[xr]
                if A[yr] < B[yr]:
                    cnt += R[yr]
                min_r, max_r = min(xr, yr), max(xr, yr)
                A[min_r] += A[max_r]
                B[min_r] += B[max_r]
                R[min_r] += R[max_r]
                R[max_r] = min_r
                if A[min_r] < B[min_r]:
                    cnt += -R[min_r]

solve()