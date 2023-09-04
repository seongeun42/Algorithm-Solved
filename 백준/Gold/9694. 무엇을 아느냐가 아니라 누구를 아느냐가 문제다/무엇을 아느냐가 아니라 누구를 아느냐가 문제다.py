import sys, heapq
input = sys.stdin.readline

def dijkstra(G, dp, pre):
    hq = []
    heapq.heappush(hq, (0, 0))
    while hq:
        cw, cn = heapq.heappop(hq)
        if dp[cn] < cw:
            continue
        for nw, nn in G[cn]:
            w = nw + cw
            if w < dp[nn]:
                dp[nn] = w
                pre[nn] = cn
                heapq.heappush(hq, (w, nn))

def solve():
    T = int(input())
    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        G = [[] for _ in range(M)]
        for _ in range(N):
            x, y, z = map(int, input().split())
            G[x].append((z, y))
            G[y].append((z, x))
        dp = [1e9] * M
        dp[0] = 0
        pre = [0] * M
        dijkstra(G, dp, pre)
        if dp[-1] == 1e9:
            print(f"Case #{tc}: -1")
        else:
            ans = [str(M - 1)]
            idx = M - 1
            while idx != 0:
                ans.append(str(pre[idx]))
                idx = pre[idx]
            print(f"Case #{tc}: {' '.join(ans[::-1])}")

solve()