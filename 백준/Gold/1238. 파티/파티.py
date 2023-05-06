import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        s_w, s_n = heapq.heappop(hq)
        if dp[start][s_n] < s_w:
            continue
        for w, e_n in G[s_n]:
            e_w = s_w + w
            if e_w < dp[start][e_n]:
                dp[start][e_n] = e_w
                heapq.heappush(hq, (e_w, e_n))

n, m, x = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    G[a - 1].append((t, b - 1))
dp = [[1e9] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0
    dijkstra(i)

cost = [0] * n
for i in range(n):
    cost[i] = dp[x - 1][i] + dp[i][x - 1]

print(max(cost))