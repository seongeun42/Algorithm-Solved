import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N = int(input())
    cost = [[*map(int, input().split())] for _ in range(N)]
    E = []
    for i in range(N):
        for j in range(i + 1, N):
            E.append((cost[i][j], i, j))
    E.sort()
    R = [i for i in range(N)]
    connected = 0
    ans = 0
    new_connected = []
    for c, u, v in E:
        if connected == N and c > 0:
            break
        ur = find_root(u, R)
        vr = find_root(v, R)
        if ur != vr:
            R[max(ur, vr)] = min(ur, vr)
            connected += 1
            if c > 0:
                ans += c
                new_connected.append((u, v))
        if c < 0:
            ans += -c
    print(ans, len(new_connected))
    for u, v in new_connected:
        print(u + 1, v + 1)

solve()