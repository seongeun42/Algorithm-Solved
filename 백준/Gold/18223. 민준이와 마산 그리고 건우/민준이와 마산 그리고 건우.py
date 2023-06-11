import sys, heapq
input = sys.stdin.readline

def dijkstra(s, dp):
    hq = []
    heapq.heappush(hq, (0, s))
    dp[s] = 0
    while hq:
        cw, cn = heapq.heappop(hq)
        if dp[cn] < cw:
            continue
        for nn, nw in G[cn]:
            w = nw + cw
            if w < dp[nn]:
                dp[nn] = w
                heapq.heappush(hq, (w, nn))

V, E, P = map(int, input().split())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

vdp = [1e9] * (V + 1)
pdp = [1e9] * (V + 1)
dijkstra(1, vdp)
dijkstra(P, pdp)
print("SAVE HIM" if vdp[V] == (vdp[P] + pdp[V]) else "GOOD BYE")