import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        cw, cn = heapq.heappop(hq)
        if dp[cn] < cw:
            continue
        for nw, nn in G[cn]:
            if nw + cw < dp[nn]:
                dp[nn] = nw + cw
                heapq.heappush(hq, (nw + cw, nn))

N = int(input())
live = set([*map(int, input().split())])
M = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    D, E, L = map(int, input().split())
    G[D].append((L, E))
    G[E].append((L, D))
dist = [[] for _ in range(N + 1)]
for l in live:
    dp = [1e9] * (N + 1)
    dp[l] = 0
    dijkstra(l)
    for i in range(1, N + 1):
        if i not in live:
            dist[i].append(dp[i])
ans = [0, 0]
for i in range(len(dist)):
    if not dist[i]: continue
    d = min(dist[i])
    if ans[0] < d or ans[0] == d and ans[1] > i:
        ans = [d, i]
print(ans[1])