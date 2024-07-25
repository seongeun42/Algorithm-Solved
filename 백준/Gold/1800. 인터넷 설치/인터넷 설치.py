import sys, heapq
input = sys.stdin.readline

def dijkstra(limit, N, K, G):
    dp = [1e9] * (N + 1)
    dp[1] = 0
    hq = []
    heapq.heappush(hq, (0, 1))
    while hq:
        cw, cn = heapq.heappop(hq)
        if dp[cn] < cw:
            continue
        for cost, nn in G[cn]:
            nw = 1 if cost > limit else 0
            if cw + nw < dp[nn]:
                dp[nn] = cw + nw
                heapq.heappush(hq, (cw + nw, nn))
    return dp[N] <= K

def solve():
    N, P, K = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(P):
        u, v, c = map(int, input().split())
        G[u].append((c, v))
        G[v].append((c, u))
    s, e = 0, 1_000_001
    ans = 1_000_001
    while s <= e:
        mid = (s + e) // 2
        isOk = dijkstra(mid, N, K, G)
        if isOk:
            e = mid - 1
            ans = mid
        else:
            s = mid + 1
    print(ans if ans != 1_000_001 else -1)

solve()