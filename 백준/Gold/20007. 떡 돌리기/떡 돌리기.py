import sys, heapq
input = sys.stdin.readline

def dijkstra(N, Y, G):
    dp = [1e9] * N
    dp[Y] = 0
    hq = []
    heapq.heappush(hq, (0, Y))
    while hq:
        cw, cn = heapq.heappop(hq)
        if dp[cn] < cw:
            continue
        for nn, nw in G[cn]:
            w = cw + nw
            if w < dp[nn]:
                dp[nn] = w
                heapq.heappush(hq, (w, nn))
    return dp

def solve():
    N, M, X, Y = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        G[a].append((b, c))
        G[b].append((a, c))
    dist = sorted(dijkstra(N, Y, G))
    ans = 1
    day_move = 0
    for d in dist:
        if d * 2 > X:
            print(-1)
            return
        if day_move + (d * 2) > X:
            ans += 1
            day_move = d * 2
        else:
            day_move += d * 2
    print(ans)
    return

solve()