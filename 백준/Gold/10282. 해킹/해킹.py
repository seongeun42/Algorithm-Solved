import sys, heapq
input = sys.stdin.readline

def Dijkstra(s):
    q = []
    heapq.heappush(q, [0, s])
    dp = [1e9] * (n + 1)
    dp[s] = 0
    while q:
        s_w, s_n = heapq.heappop(q)
        if dp[s_n] < s_w:
            continue
        for w, e_n in G[s_n]:
            e_w = w + s_w
            if e_w < dp[e_n]:
                dp[e_n] = e_w
                heapq.heappush(q, [e_w, e_n])
    print(n - dp.count(1e9) + 1, end=' ')
    time = 0
    for v in dp:
        if v != 1e9:
            time = max(time, v)
    print(time)

T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    G = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        G[b].append([s, a])
    Dijkstra(c)