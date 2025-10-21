import sys, heapq
input = sys.stdin.readline

def dijkstra(N, G, start, speed):
    dp = [1e11] * (N + 1)
    dp[start] = 0
    hq = [(0, start)]
    while hq:
        c_w, c_n = heapq.heappop(hq)
        if dp[c_n] < c_w:
            continue
        for n_n, dist in G[c_n]:
            w = c_w + speed * dist
            if w < dp[n_n]:
                dp[n_n] = w
                heapq.heappush(hq, (w, n_n))
    return dp

def solve():
    T = int(input())
    for t in range(T):
        N, P, M = map(int, input().split())
        friends = [[*map(int, input().split())] for _ in range(P)]
        G = [[] for _ in range(N + 1)]
        for _ in range(M):
            load = [*map(int, input().split())]
            for i in range(2, len(load) - 1):
                G[load[i]].append((load[i + 1], load[0]))
                G[load[i + 1]].append((load[i], load[0]))
        cities = []
        for f in friends:
            cities.append(dijkstra(N, G, f[0], f[1]))
        cities = list(zip(*cities))
        ans = 1e11
        for c in cities:
            time = max(c)
            if time < ans:
                ans = time
        print(f"Case #{t + 1}: {ans if ans != 1e11 else -1}")

solve()