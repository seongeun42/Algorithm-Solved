import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    dp[start][start] = 0
    while hq:
        s_w, s_n = heapq.heappop(hq)
        if dp[start][s_n] < s_w:
            continue
        for w, e_n in G[s_n]:
            e_w = s_w + w
            if e_w < dp[start][e_n]:
                dp[start][e_n] = e_w
                heapq.heappush(hq, (e_w, e_n))

n, m, r = map(int, input().split())
item = [0] + [*map(int, input().split())]
G = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    G[a].append((l, b))
    G[b].append((l, a))

dp = [[1e9] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dijkstra(i)

ans = 0
for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if dp[i][j] <= m:
            cnt += item[j]
    ans = max(ans, cnt)
print(ans)