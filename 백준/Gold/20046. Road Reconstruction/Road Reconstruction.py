import sys, heapq
input = sys.stdin.readline

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def dijkstra(dp, road, m, n):
    hq = [(dp[0][0], 0, 0)]
    while hq:
        cw, cy, cx = heapq.heappop(hq)
        if cw < dp[cy][cx]:
            continue
        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if 0 <= ny < m and 0 <= nx < n and road[ny][nx] >= 0:
                w = cw + road[ny][nx]
                if w < dp[ny][nx]:
                    dp[ny][nx] = w
                    heapq.heappush(hq, (w, ny, nx))

def solve():
    m, n = map(int, input().split())
    road = [[*map(int, input().split())] for _ in range(m)]
    dp = [[1e9] * n for _ in range(m)]
    if road[0][0] != -1:
        dp[0][0] = road[0][0]
        dijkstra(dp, road, m, n)
    print(dp[-1][-1] if dp[-1][-1] != 1e9 else -1)

solve()