import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    while q:
        c_w, c_n = heapq.heappop(q)
        if dp[c_n] < c_w:
            continue
        for n_w, n_n in G[c_n]:
            w = c_w + n_w
            if w < dp[n_n]:
                dp[n_n] = w
                heapq.heappush(q, [w, n_n])

T, C, Ts, Te = map(int, input().split())
G = [[] for _ in range(T + 1)]
for _ in range(C):
    u, v, w = map(int, input().split())
    G[u].append([w, v])
    G[v].append([w, u])
dp = [1e9] * (T + 1)
dp[Ts] = 0
dijkstra(Ts)
print(dp[Te])