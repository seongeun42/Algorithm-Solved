import sys, heapq
input = sys.stdin.readline

def dijkstra(G, start):
    hq = [(0, start)]
    dp = [1e9] * len(G)
    dp[start] = 0
    while hq:
        cw, cn = heapq.heappop(hq)
        if dp[cn] < cw:
            continue
        for nn, nw in G[cn]:
            w = cw + nw
            if w < dp[nn]:
                dp[nn] = w
                heapq.heappush(hq, (w, nn))
    return dp

def solve():
    V, M = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        G[a].append((b, c))
        G[b].append((a, c))
    J, S = map(int, input().split())
    jtime = dijkstra(G, J)
    stime = dijkstra(G, S)
    candi = []
    dist = 2e9
    for i in range(1, V + 1):
        if i == J or i == S:
            continue
        hap = jtime[i] + stime[i]
        if hap < dist:
            dist = hap
            candi = [i]
        elif hap == dist:
            candi.append(i)
    ans = -1
    for c in candi:
        if jtime[c] > stime[c]:
            continue
        if ans == -1 or jtime[c] < jtime[ans]:
            ans = c
    print(ans)

solve()