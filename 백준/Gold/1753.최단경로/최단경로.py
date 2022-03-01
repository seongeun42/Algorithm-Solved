import sys, heapq
input = sys.stdin.readline

def Dijkstra(s):
    q = []
    heapq.heappush(q, [0, s])
    while q:
        s_weight, s_node = heapq.heappop(q)
        if dp[s_node] < s_weight:
            continue
        for w, e_node in G[s_node]:
            e_weight = w + s_weight
            if e_weight < dp[e_node]:
                dp[e_node] = e_weight
                heapq.heappush(q, [e_weight, e_node])

V, E = map(int, input().split())
S = int(input())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    if u > V or v > V: continue
    G[u].append([w, v])
dp = [1e9] * (V + 1)
dp[S] = 0
Dijkstra(S)
for v in dp[1:]:
    print(v if v != 1e9 else "INF")