import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N = int(input())
    # x, y, z 각각 저장 후 정렬
    x, y, z = [], [], []
    for i in range(N):
        xi, yi, zi = map(int, input().split())
        x.append((xi, i))
        y.append((yi, i))
        z.append((zi, i))
    x.sort(); y.sort(); z.sort()
    # 정렬 후 인접한 행성끼리만 연결 비용 계산
    cost = []
    for i in range(1, N):
        cost.append((x[i][0] - x[i - 1][0], x[i][1], x[i - 1][1]))
        cost.append((y[i][0] - y[i - 1][0], y[i][1], y[i - 1][1]))
        cost.append((z[i][0] - z[i - 1][0], z[i][1], z[i - 1][1]))
    cost.sort()
    # 최소 비용 구하기
    R = [i for i in range(N)]
    connected = 1
    ans = 0
    for c, u, v in cost:
        if connected == N:
            break
        ur = find_root(u, R)
        vr = find_root(v, R)
        if ur != vr:
            R[max(ur, vr)] = min(ur, vr)
            connected += 1
            ans += c
    print(ans)

solve()