import sys, heapq
input = sys.stdin.readline

def dijkstra(V, G, S):
    dp = [1e9] * (V + 1)
    dp[S] = 0
    hq = [(0, S)]
    heapq.heapify(hq)
    while hq:
        cw, cn = heapq.heappop(hq)
        if dp[cn] < cw:
            continue
        for nn, nw in G[cn]:
            w = cw + nw
            if w < dp[nn]:
                dp[nn] = w
                heapq.heappush(hq, (w, nn))
    for i in range(V + 1):
        if dp[i] == 1e9:
            dp[i] = -1
    return dp

def solve():
    N, V, E = map(int, input().split())
    A, B = map(int, input().split())
    team = [*map(int, input().split())]
    G = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b, l = map(int, input().split())
        G[a].append((b, l))
        G[b].append((a, l))
    kist = dijkstra(V, G, A)
    crfood = dijkstra(V, G, B)
    ans = 0
    for t in team:
        ans += kist[t] + crfood[t]
    print(ans)

solve()