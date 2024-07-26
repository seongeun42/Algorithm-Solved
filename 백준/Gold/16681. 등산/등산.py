import sys, heapq
input = sys.stdin.readline

def dijkstra(s, N, h, G):
    hq = []
    dp = [float("inf")] * (N + 1)
    dp[s] = 0
    heapq.heappush(hq, (0, s))
    while hq:
        cw, cn = heapq.heappop(hq)
        if dp[cn] < cw:
            continue
        for nw, nn in G[cn]:
            if h[cn] < h[nn] and cw + nw < dp[nn]:
                dp[nn] = cw + nw
                heapq.heappush(hq, (cw + nw, nn))
    return dp

def solve():
    N, M, D, E = map(int, input().split())
    h = [0] + [*map(int, input().split())]
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, n = map(int, input().split())
        G[a].append((n, b))
        G[b].append((n, a))
    up = dijkstra(1, N, h, G)
    down = dijkstra(N, N, h, G)
    inf = float("inf")
    ans = -inf
    for i in range(2, N):
        if up[i] == inf or down[i] == inf:
            continue
        v = h[i] * E - (up[i] + down[i]) * D
        if ans < v:
            ans = v
    print(ans if ans != -inf else "Impossible")

solve()