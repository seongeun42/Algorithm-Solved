import sys, heapq
input = sys.stdin.readline

def dijkstra(start, N, G):
    hq = [(0, start)]
    heapq.heapify(hq)
    dp = [1e9] * (N + 1)
    while hq:
        cw, cn = heapq.heappop(hq)
        if dp[cn] < cw:
            continue
        for nw, nn in G[cn]:
            w = cw + nw
            if w < dp[nn]:
                dp[nn] = w
                heapq.heappush(hq, (w, nn))
    return dp

def solve():
    N, M = map(int, input().split())
    j = int(input())
    K = int(input())
    A = [*map(int, input().split())]
    B = [*map(int, input().split())]
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        X, Y, Z = map(int, input().split())
        G[X].append((Z, Y))
        G[Y].append((Z, X))
    dists = dijkstra(j, N, G)
    h_type, h_dist = '', 1e9
    for i in range(K):
        if dists[A[i]] < h_dist:
            h_type, h_dist = 'A', dists[A[i]]
        if dists[B[i]] < h_dist:
            h_type, h_dist = 'B', dists[B[i]]
    if h_dist != 1e9:
        print(h_type, h_dist, sep="\n")
    else:
        print(-1)

solve()