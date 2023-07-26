import sys, heapq
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def Dijkstra():
    hq = []
    heapq.heappush(hq, (0, 0, 0))
    while hq:
        cw, cx, cy = heapq.heappop(hq)
        if dp[cy][cx] < cw:
            continue
        for  i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                w = max(abs(G[cy][cx] - G[ny][nx]), cw)
                if w < dp[ny][nx]:
                    dp[ny][nx] = w
                    heapq.heappush(hq, (w, nx, ny))

N = int(input())
G = [[*map(int, input().split())] for _ in range(N)]
dp = [[1e9] * N for _ in range(N)]
dp[0][0] = 0
Dijkstra()
print(dp[-1][-1])