import sys, heapq
input = sys.stdin.readline

def Dijkstra(s):
    q = []
    heapq.heappush(q, [0, s])
    dp[s][s] = 0
    while q:
        s_w, s_n = heapq.heappop(q)
        if dp[s][s_n] < s_w:
            continue
        for w, e_n in G[s_n]:
            e_w = w + s_w
            if e_w < dp[s][e_n]:
                dp[s][e_n] = e_w
                res[e_n - 1][s - 1] = s_n
                heapq.heappush(q, [e_w, e_n])

N, M = map(int, input().split())
res = [['-'] * N for _ in range(N)]
G = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, Time = map(int, input().split())
    G[A].append([Time, B])
    G[B].append([Time, A])
dp = [[1e9] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    Dijkstra(i)

for v in res:
    print(*v)