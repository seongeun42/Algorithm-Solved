import sys, heapq
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dijkstra():
    hq = []
    heapq.heappush(hq, (0, 0, 0))
    while hq:
        s_w, s_y, s_x = heapq.heappop(hq)
        if dp[s_y][s_x] < s_w:
            continue
        for i in range(4):
            ny, nx = s_y + dy[i], s_x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                w = 1 if room[ny][nx] == "0" else 0
                if w + s_w < dp[ny][nx]:
                    dp[ny][nx] = w + s_w
                    heapq.heappush(hq, (w + s_w, ny, nx))

n = int(input())
room = [input().strip() for _ in range(n)]
dp = [[1e9] * n for _ in range(n)]
dp[0][0] = 0
dijkstra()
print(dp[-1][-1])