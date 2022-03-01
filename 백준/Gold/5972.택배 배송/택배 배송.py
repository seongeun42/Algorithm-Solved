import sys, heapq
input = sys.stdin.readline

def Dijkstra():
    q = []
    heapq.heappush(q, [0, 1])
    while q:
        s_w, s_n = heapq.heappop(q)
        if dp[s_n] < s_w:
            continue
        for w, e_n in G[s_n]:
            e_w = w + s_w
            if e_w < dp[e_n]:
                dp[e_n] = e_w
                heapq.heappush(q, [e_w, e_n])

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    G[s].append([w, e])
    G[e].append([w, s])
dp = [1e9] * (N + 1)
dp[1] = 0
Dijkstra()
print(dp[N])