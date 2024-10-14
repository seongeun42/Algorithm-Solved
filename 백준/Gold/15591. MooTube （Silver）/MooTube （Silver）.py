import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] < 0:
        return n
    R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N, Q = map(int, input().split())
    E = sorted([[*map(int, input().split())] for _ in range(N - 1)], key=lambda x: x[2])
    queries = sorted([[*map(int, input().split())] + [i] for i in range(Q)], key=lambda x: -x[0])
    R = [-1] * (N + 1)
    ans = []
    for k, v, idx in queries:
        while E and E[-1][2] >= k:
            p, q, r = E.pop()
            pr = find_root(p, R)
            qr = find_root(q, R)
            if pr < qr:
                R[pr] += R[qr]
                R[qr] = pr
            elif pr > qr:
                R[qr] += R[pr]
                R[pr] = qr
        vr = find_root(v, R)
        ans.append((idx, -R[vr] - 1))
    ans.sort()
    for idx, cnt in ans:
        print(cnt)
        
solve()