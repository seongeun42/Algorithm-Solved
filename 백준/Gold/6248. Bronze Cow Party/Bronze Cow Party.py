import sys, heapq
input = sys.stdin.readline

def solve():
    N, M, X = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, t = map(int, input().split())
        G[a].append((t, b))
        G[b].append((t, a))
    hq = [(0, X)]
    dp = [1e9] * (N + 1)
    dp[X] = 0
    while hq:
        cw, cn = heapq.heappop(hq)
        if cw < dp[cn]:
            continue
        for nw, nn in G[cn]:
            w = cw + nw
            if w < dp[nn]:
                dp[nn] = w
                heapq.heappush(hq, (w, nn))
    ans = 0
    for time in dp:
        if time == 1e9:
            continue
        if time > ans:
            ans = time
    print(ans * 2)

solve()