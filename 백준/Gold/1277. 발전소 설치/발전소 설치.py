import sys, heapq, math
input = sys.stdin.readline

def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    dp = [1e9] * (N + 1)
    dp[1] = 0
    while q:
        c_w, c_n = heapq.heappop(q)
        if dp[c_n] < c_w:
            continue
        for n_n, n_w in G[c_n]:
            w = c_w + n_w
            if w < dp[n_n]:
                dp[n_n] = w
                heapq.heappush(q, (w, n_n))
    return dp[N]

N, W = map(int, input().split())
M = float(input())
plant = [[*map(int, input().split())] for _ in range(N)]
G = [[] for _ in range(N + 1)]
for _ in range(W):
    p1, p2 = map(int, input().split())
    G[p1].append((p2, 0))
    G[p2].append((p1, 0))
for i in range(N):
    for j in range(i + 1, N):
        dist = ((plant[i][0] - plant[j][0]) ** 2 + (plant[i][1] - plant[j][1]) ** 2) ** 0.5
        if dist > M:
            continue
        G[i + 1].append((j + 1, dist))
        G[j + 1].append((i + 1, dist))
print(math.floor(dijkstra() * 1000))