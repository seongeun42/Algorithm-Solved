import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    n, Q = map(int, input().split())
    E = sorted([[*map(int, input().split())] for _ in range(Q)], key=lambda x: (x[2], x[3]))
    R = [i for i in range(n + 1)]
    connected = 1
    total = 0
    complete = 0
    for u, v, cost, time in E:
        if connected == n:
            break
        ur = find_root(u, R)
        vr = find_root(v, R)
        if ur != vr:
            R[max(ur, vr)] = min(ur, vr)
            total += cost
            connected += 1
            if complete < time:
                complete = time
    if connected == n:
        print(complete, total)
    else:
        print(-1)

solve()