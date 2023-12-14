import sys, heapq
input = sys.stdin.readline

def Dijkstra(s):
    dp = [1e9] * (N + 1)
    dp[s] = 0
    q = []
    heapq.heappush(q, [dp[s], s])
    while q:
        s_w, s_n = heapq.heappop(q)
        if dp[s_n] < s_w:
            continue
        for w, e_n in G[s_n]:
            e_w = w + s_w
            if e_w < dp[e_n]:
                dp[e_n] = e_w
                heapq.heappush(q, [e_w, e_n])
    return dp

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    G[a].append([t, b])
    G[b].append([t, a])
v1, v2 = map(int, input().split())
s_ = Dijkstra(1)
v1_ = Dijkstra(v1)
v2_ = Dijkstra(v2)
res = min(s_[v1] + v1_[v2] + v2_[N], s_[v2] + v2_[v1] + v1_[N])
print(res if res < 1e9 else -1)