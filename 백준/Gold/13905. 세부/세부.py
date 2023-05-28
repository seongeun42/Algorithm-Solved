import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (-1e9, start))
    while hq:
        s_w, s_n = heapq.heappop(hq)
        s_w = -s_w
        if dp[s_n] > s_w:
            continue
        for e_w, e_n in G[s_n]:
            w = min(e_w, s_w)
            if w > dp[e_n]:
                dp[e_n] = w
                heapq.heappush(hq, (-w, e_n))

N, M = map(int, input().split())
s, e = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    h1, h2, k = map(int, input().split())
    G[h1].append((k, h2))
    G[h2].append((k, h1))
dp = [0] * (N + 1)
dp[s] = 1e9
dijkstra(s)
print(dp[e])