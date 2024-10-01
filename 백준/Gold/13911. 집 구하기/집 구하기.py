import sys, heapq
input = sys.stdin.readline

def dijkstra(V, G, S):
    dp = [1e9] * (V + 1)
    hq = []
    for s in S:
        heapq.heappush(hq, (0, s))
        dp[s] = 0
    while hq:
        cw, cn = heapq.heappop(hq)
        if dp[cn] < cw:
            continue
        for nn, nw in G[cn].items():
            w = cw + nw
            if w < dp[nn]:
                dp[nn] = w
                heapq.heappush(hq, (w, nn))
    return dp

def solve():
    V, E = map(int, input().split())
    G = [{} for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        if v in G[u]:
            G[u][v] = G[v][u] = min(G[v][u], w)
        else:
            G[u][v] = G[v][u] = w
    M, x = map(int, input().split())
    mcdonalds = [*map(int, input().split())]
    m_dist = dijkstra(V, G, mcdonalds)
    S, y = map(int, input().split())
    starbucks = [*map(int, input().split())]
    s_dist = dijkstra(V, G, starbucks)
    ans = 1e10
    for i in range(1, V + 1):
        if 0 < m_dist[i] <= x and 0 < s_dist[i] <= y:
            dist = m_dist[i] + s_dist[i]
            if dist < ans:
                ans = dist
    print(ans if ans != 1e10 else -1)

solve()