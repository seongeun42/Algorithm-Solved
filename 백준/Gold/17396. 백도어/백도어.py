import sys, heapq
input = sys.stdin.readline

def Dijkstra():
    q = []
    heapq.heappush(q, [0, 0])
    while q:
        s_w, s_n = heapq.heappop(q)
        if A[s_n] == 1 or dp[s_n] < s_w:
            continue
        for w, e_n in G[s_n]:
            e_w = w + s_w
            if e_w < dp[e_n]:
                dp[e_n] = e_w
                heapq.heappush(q, [e_w, e_n])

N, M = map(int, input().split())
A = [*map(int, input().split())]
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    G[a].append([t, b])
    G[b].append([t, a])
dp = [1e12] * N
dp[0] = 0
Dijkstra()
print(dp[-1] if dp[-1] != 1e12 else -1)