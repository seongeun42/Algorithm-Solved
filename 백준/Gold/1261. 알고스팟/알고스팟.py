import sys, heapq
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def Dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))
    while q:
        s_w, sy, sx = heapq.heappop(q)
        if dp[sy][sx] < s_w:
            continue
        for i in range(4):
            ny, nx = sy + dy[i], sx + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                w = 1 if miro[ny][nx] == "1" else 0
                if w + s_w < dp[ny][nx]:
                    dp[ny][nx] = w + s_w
                    heapq.heappush(q, (w + s_w, ny, nx))

m, n = map(int, input().split())
miro = [input() for _ in range(n)]
dp = [[1e9] * m for _ in range(n)]
dp[0][0] = 0
Dijkstra()
print(dp[n - 1][m - 1])