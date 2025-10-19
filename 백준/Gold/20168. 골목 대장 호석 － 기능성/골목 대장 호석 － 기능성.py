import sys, heapq
input = sys.stdin.readline

def dijkstra(N, A, B, C, G):
    dp = [1e9] * (N + 1)
    dp[A] = 0
    hq = []
    heapq.heappush(hq, (0, 0, A))
    while hq:
        c_w, c_c, c_n = heapq.heappop(hq)
        if dp[c_n] < c_w:
            continue
        for n_w, n_n in G[c_n]:
            if c_c + n_w <= C:
                w = max(c_w, n_w)
                if w < dp[n_n]:
                    dp[n_n] = w
                    heapq.heappush(hq, (w, c_c + n_w, n_n))
    return dp[B] if dp[B] != 1e9 else -1


def solve():
    N, M, A, B, C = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        G[u].append((w, v))
        G[v].append((w, u))
    print(dijkstra(N, A, B, C, G))

solve()