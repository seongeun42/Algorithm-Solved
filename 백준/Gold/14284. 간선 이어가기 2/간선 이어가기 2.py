import sys, heapq
input = sys.stdin.readline

def dijkstra(s):
    hq = []
    heapq.heappush(hq, (0, s))
    dp[s] = 0
    while hq:
        c_w, c_n = heapq.heappop(hq)
        if dp[c_n] < c_w:
            continue
        for n_n, n_w in G[c_n]:
            w = n_w + c_w
            if w < dp[n_n]:
                dp[n_n] = w
                heapq.heappush(hq, (w, n_n))

n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))
s, t = map(int, input().split())
dp = [1e9] * (n + 1)
dijkstra(s)
print(dp[t])