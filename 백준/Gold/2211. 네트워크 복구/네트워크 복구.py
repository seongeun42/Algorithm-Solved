import sys, heapq
input = sys.stdin.readline

def dijkstra(start, G, dp):
    q = []
    dp[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        cw, cn = heapq.heappop(q)
        if dp[cn] < cw:
            continue
        for nn, nw in G[cn]:
            w = cw + nw
            if w < dp[nn]:
                parent[nn] = cn
                dp[nn] = w
                heapq.heappush(q, (w, nn))

if __name__ == "__main__":
    n, m = map(int, input().split())
    dp = [1e9] * (n + 1)
    parent = [0] * (n + 1)
    G = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        G[a].append((b, c))
        G[b].append((a, c))

    dijkstra(1, G, dp)

    print(n - 1)
    for i in range(2, n + 1):
        print(i, parent[i])