import sys, heapq
input = sys.stdin.readline

def prim(G, YNY):
    hq = []
    visit = [0] * len(G)
    cnt = 0
    for v in YNY:
        visit[v] = 1
        cnt += 1
        for e in G[v]:
            heapq.heappush(hq, e)
    total = 0
    while hq:
        w, e = heapq.heappop(hq)
        if not visit[e]:
            visit[e] = 1
            cnt += 1
            total += w
            for edge in G[e]:
                if not visit[edge[1]]:
                    heapq.heappush(hq, edge)
        if cnt == len(G):
            break
    return total

def solve():
    N, M, K = map(int, input().split())
    YNY = [*map(int, input().split())]
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        G[u].append((w, v))
        G[v].append((w, u))
    print(prim(G, YNY))

solve()