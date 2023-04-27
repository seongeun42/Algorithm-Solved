import sys, heapq
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def miroCreate(mod):
    for _ in range(int(input())):
        x1, y1, x2, y2 = map(int, input().split())
        lx, rx = min(x1, x2), max(x1, x2)
        uy, dy = min(y1, y2), max(y1, y2)
        for i in range(uy, dy + 1):
            for j in range(lx, rx + 1):
                miro[i][j] = mod

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))
    dp[0][0] = 0
    while q:
        s_w, sy, sx = heapq.heappop(q)
        if dp[sy][sx] < s_w:
            continue
        for i in range(4):
            ny, nx = sy + dy[i], sx + dx[i]
            if 0 <= ny <= 500 and 0 <= nx <= 500 and miro[ny][nx] != -1:
                w = s_w + miro[ny][nx]
                if w < dp[ny][nx]:
                    dp[ny][nx] = w
                    heapq.heappush(q, (w, ny, nx))

miro = [[0] * 501 for _ in range(501)]
miroCreate(1)
miroCreate(-1)
dp = [[1e9] * 501 for _ in range(501)]
dijkstra()
print(dp[-1][-1] if dp[-1][-1] != 1e9 else -1)