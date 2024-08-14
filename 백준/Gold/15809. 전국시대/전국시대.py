import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N, M = map(int, input().split())
    A = [0] + [int(input()) for _ in range(N)]
    R = [i for i in range(N + 1)]
    for _ in range(M):
        O, P, Q = map(int, input().split())
        pr = find_root(P, R)
        qr = find_root(Q, R)
        if O == 1:
            if pr < qr:
                R[qr] = pr
                A[pr] += A[qr]
            else:
                R[pr] = qr
                A[qr] += A[pr]
        else:
            if A[pr] > A[qr]:
                R[qr] = pr
                A[pr] -= A[qr]
            elif A[pr] < A[qr]:
                R[pr] = qr
                A[qr] -= A[pr]
            else:
                R[qr] = R[pr] = 0
                A[qr] = A[pr] = 0
    ans = []
    for i in range(1, N + 1):
        if R[i] == i:
            ans.append(A[i])
    ans.sort()
    print(len(ans))
    print(*ans)

solve()