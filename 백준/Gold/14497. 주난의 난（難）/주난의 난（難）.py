import sys, heapq
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dijkstra(sx, sy):
    hq = []
    heapq.heappush(hq, (0, sx, sy))
    dp[sy][sx] = 0
    while hq:
        cw, cx, cy = heapq.heappop(hq)
        if dp[cy][cx] < cw:
            continue
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                w = cw if room[ny][nx] == '0' else cw + 1
                if w < dp[ny][nx]:
                    dp[ny][nx] = w
                    heapq.heappush(hq, (w, nx, ny))

N, M = map(int, input().split())
y1, x1, y2, x2 = map(int, input().split())
room = [input().rstrip() for _ in range(N)]
dp = [[1e9] * M for _ in range(N)]
dijkstra(x1 - 1, y1 - 1)
print(dp[y2 - 1][x2 - 1])