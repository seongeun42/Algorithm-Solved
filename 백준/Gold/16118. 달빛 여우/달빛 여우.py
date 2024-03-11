import sys, heapq
input = sys.stdin.readline

def fox_move(G, N):
    dp = [1e12] * (N + 1)
    dp[1] = 0
    hq = []
    heapq.heappush(hq, (0, 1))
    while hq:
        c_w, c_n = heapq.heappop(hq)
        if dp[c_n] < c_w:
            continue
        for n_w, n_n in G[c_n]:
            w = n_w + c_w
            if w < dp[n_n]:
                dp[n_n] = w
                heapq.heappush(hq, (w, n_n))
    return dp


def wolf_move(G, N, S):
    dp = [[1e12, 1e12] for _ in range(N + 1)]
    # dp[S] = [0, 0]
    hq = []
    heapq.heappush(hq, (0, S, 0))
    while hq:
        c_w, c_n, flag = heapq.heappop(hq)
        if dp[c_n][flag] < c_w:
            continue
        for n_w, n_n in G[c_n]:
            multi = 0.5 if flag == 0 else 2
            w = n_w * multi + c_w
            if w < dp[n_n][abs(flag - 1)]:
                dp[n_n][abs(flag - 1)] = w
                heapq.heappush(hq, (w, n_n, abs(flag - 1)))
    return dp


def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, d = map(int, input().split())
        G[a].append([d, b])
        G[b].append([d, a])
    fox = fox_move(G, N)
    wolf = wolf_move(G, N, 1)
    ans = 0
    for i in range(2, N + 1):
        if fox[i] < min(wolf[i]):
            ans += 1
    print(ans)

solve()