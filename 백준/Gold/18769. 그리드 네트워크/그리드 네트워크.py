import sys, heapq
input = sys.stdin.readline

def prim(G, R, C):
    hq = G[0]
    heapq.heapify(hq)
    visited = [0] * (R * C)
    visited[0] = 1
    res = 0
    while hq:
        w, e = heapq.heappop(hq)
        if not visited[e]:
            visited[e] = 1
            res += w
            for nw, ne in G[e]:
                if not visited[ne]:
                    heapq.heappush(hq, (nw, ne))
    return res

def solve():
    T = int(input())
    for _ in range(T):
        R, C = map(int, input().split())
        G = [[] for _ in range(R * C)]
        for i in range(R):
            c = [*map(int, input().split())]
            for j in range(C - 1):
                n = i * C + j
                G[n].append((c[j], n + 1))
                G[n + 1].append((c[j], n))
        for i in range(R - 1):
            c = [*map(int, input().split())]
            for j in range(C):
                n = i * C + j
                G[n].append((c[j], n + C))
                G[n + C].append((c[j], n))
        print(prim(G, R, C))

solve()