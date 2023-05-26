import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        s_w, s_n = heapq.heappop(hq)
        if dp[s_n] < s_w:
            continue
        for e_w, e_n in G[s_n]:
            w = e_w + s_w
            if w < dp[e_n]:
                dp[e_n] = w
                heapq.heappush(hq, (w, e_n))

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        G[a].append((c, b))
        G[b].append((c, a))
    K = int(input())
    loca = [*map(int, input().split())]
    dist = [[0, i] for i in range(N + 1)]
    for l in loca:
        dp = [1e9] * (N + 1)
        dp[l] = 0
        dijkstra(l)
        for i in range(1, N + 1):
            dist[i][0] += dp[i]
    dist.sort(key=lambda x: (x[0], x[1]))
    print(dist[1][1])