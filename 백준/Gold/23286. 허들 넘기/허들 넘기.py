import sys, heapq
input = sys.stdin.readline

def dijstra(start, G, N):
    height = [1e9] * (N + 1)
    height[start] = 0
    hq = [(0, start)]
    while hq:
        cw, cn = heapq.heappop(hq)
        if height[cn] < cw:
            continue
        for nn, nw in G[cn]:
            w = max(cw, nw)
            if w < height[nn]:
                height[nn] = w
                heapq.heappush(hq, (w, nn))
    return height

def solve():
    N, M, T = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, h = map(int, input().split())
        G[u].append((v, h))
    tc = []
    starts = {}
    for _ in range(T):
        s, e = map(int, input().split())
        if s not in starts:
            starts[s] = None
        tc.append((s, e))
    for s in starts:
        starts[s] = dijstra(s, G, N)
    for s, e in tc:
        h = starts[s][e]
        print(h if h != 1e9 else -1)

solve()