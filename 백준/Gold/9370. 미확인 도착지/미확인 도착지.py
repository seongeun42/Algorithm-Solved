import sys, heapq
input = sys.stdin.readline

def dijkstra(s, dp):
    hq = []
    heapq.heappush(hq, (0, s, 0))
    dp[s] = 0
    while hq:
        s_w, s_n, gh = heapq.heappop(hq)
        if dp[s_n] < s_w:
            continue
        for w, e_n in G[s_n]:
            e_w = w + s_w
            if e_w < dp[e_n]:
                dp[e_n] = e_w
                heapq.heappush(hq, (e_w, e_n, gh))

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    G = [[] for _ in range(n + 1)]
    ghd = 0
    for _ in range(m):
        a, b, d = map(int, input().split())
        G[a].append((d, b))
        G[b].append((d, a))
        if {a, b} == {g, h}:
            ghd = d
    candi = sorted([int(input()) for _ in range(t)])
    dpS = [1e9] * (n + 1)
    dpG = [1e9] * (n + 1)
    dpH = [1e9] * (n + 1)
    dijkstra(s, dpS)
    dijkstra(g, dpG)
    dijkstra(h, dpH)
    ans = []
    for c in candi:
        if dpS[c] in {dpS[h] + ghd + dpG[c], dpS[g] + ghd + dpH[c]}:
            ans.append(c)
    print(*ans)