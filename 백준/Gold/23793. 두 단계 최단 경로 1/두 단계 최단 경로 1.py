import sys, heapq
input = sys.stdin.readline

def dijkstra(start, G, exception):
    dp = [1e9] * len(G)
    dp[start] = 0
    hq = [(0, start)]
    while hq:
        cw, cn = heapq.heappop(hq)
        if dp[cn] < cw:
            continue
        for nw, nn in G[cn]:
            if nn == exception:
                continue
            w = cw + nw
            if w < dp[nn]:
                dp[nn] = w
                heapq.heappush(hq, (w, nn))
    return dp

def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        G[u].append((w, v))
    x, y, z = map(int, input().split())
    x_start = dijkstra(x, G, -1)
    y_start = dijkstra(y, G, -1)
    x_start_no_y = dijkstra(x, G, y)
    xyz = x_start[y] + y_start[z]
    xz = x_start_no_y[z]
    print(xyz if x_start[y] != 1e9 and y_start[z] != 1e9 else -1, xz if xz != 1e9 else -1)

solve()