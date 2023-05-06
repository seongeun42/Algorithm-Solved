import sys, heapq
input = sys.stdin.readline

def dijkstra(start, G, dp):
    hq = []
    heapq.heappush(hq, (0, start))
    dp[start] = 0
    while hq:
        s_w, s_n = heapq.heappop(hq)
        if dp[s_n] < s_w:
            continue
        for w, e_n in G[s_n]:
            e_w = s_w + w
            if e_w < dp[e_n]:
                dp[e_n] = e_w
                heapq.heappush(hq, (e_w, e_n))

n, m, x = map(int, input().split())
G_GO = [[] for _ in range(n)]
G_BACK = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    G_GO[a - 1].append((t, b - 1))
    G_BACK[b - 1].append((t, a - 1))
go = [1e9] * n
back = [1e9] * n
dijkstra(x - 1, G_GO, go)
dijkstra(x - 1, G_BACK, back)
print(max([go[i] + back[i] for i in range(n)]))