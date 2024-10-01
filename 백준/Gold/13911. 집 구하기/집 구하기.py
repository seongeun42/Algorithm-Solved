import sys, heapq
input = sys.stdin.readline

def dijkstra(V, G, W, S):
    dp = [1e9] * (V + 1)
    hq = []
    for s in S:
        heapq.heappush(hq, (0, s))
        dp[s] = 0
    while hq:
        cw, cn = heapq.heappop(hq)
        if dp[cn] < cw:
            continue
        for nn in G[cn]:
            w = cw + W[(cn, nn)]
            if w < dp[nn]:
                dp[nn] = w
                heapq.heappush(hq, (w, nn))
    return dp

def solve():
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    W = {}
    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
        if (u, v) not in W or W[(u, v)] > w:
            W[(u, v)] = w
            W[(v, u)] = w
    M, x = map(int, input().split())
    mcdonalds = set(map(int, input().split()))
    m_dist = dijkstra(V, G, W, mcdonalds)
    S, y = map(int, input().split())
    starbucks = set(map(int, input().split()))
    s_dist = dijkstra(V, G, W, starbucks)
    ans = 1e10
    for i in range(1, V + 1):
        if i in mcdonalds or i in starbucks:
            continue
        if m_dist[i] > x or s_dist[i] > y:
            continue
        dist = m_dist[i] + s_dist[i]
        if dist < ans:
            ans = dist
    print(ans if ans != 1e10 else -1)

solve()