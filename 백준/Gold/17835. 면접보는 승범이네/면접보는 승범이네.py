import sys, heapq
input = sys.stdin.readline

def solve():
    N, M, K = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        U, V, C = map(int, input().split())
        G[V].append((C, U))
    destination = [*map(int, input().split())]
    dp = [float("inf")] * (N + 1)
    hq = []
    for s in destination:
        heapq.heappush(hq, (0, s))
        dp[s] = 0
    while hq:
        sw, sn = heapq.heappop(hq)
        if dp[sn] < sw:
            continue
        for nw, nn in G[sn]:
            if sw + nw < dp[nn]:
                dp[nn] = sw + nw
                heapq.heappush(hq, (sw + nw, nn))
    city, dist = 0, 0
    for i in range(1, N + 1):
        if dp[i] == float("inf"):
            continue
        if dist < dp[i]:
            city, dist = i, dp[i]
    print(city, dist, sep="\n")

solve()