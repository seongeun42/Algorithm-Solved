import sys, heapq
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dijkstra(sx, sy):
    hq = []
    for i in range(4):
        nx, ny = sx + dx[i], sy + dy[i]
        if 0 <= nx < n and 0 <= ny < n and home[ny][nx] != "*":
            dp[sy][sx][i] = 0
            heapq.heappush(hq, (0, sx, sy, i))

    while hq:
        ccnt, cx, cy, cd = heapq.heappop(hq)
        if dp[cy][cx][cd] < ccnt:
            continue
        nx, ny = cx + dx[cd], cy + dy[cd]
        if 0 <= nx < n and 0 <= ny < n and home[ny][nx] != "*":
            if home[ny][nx] in [".", "#"] and ccnt < dp[ny][nx][cd]:
                dp[ny][nx][cd] = ccnt
                heapq.heappush(hq, (ccnt, nx, ny, cd))
            elif home[ny][nx] == "!":
                for i in range(4):
                    w = 1 if i != cd else 0
                    if ccnt + w < dp[ny][nx][i]:
                        dp[ny][nx][i] = ccnt + w
                    heapq.heappush(hq, (ccnt + w, nx, ny, i))

n = int(input())
home = [input().strip() for _ in range(n)]
door = []
for i in range(n):
    for j in range(n):
        if home[i][j] == "#":
            door.append((j, i))
dp = [[[1e9] * 4 for _ in range(n)] for _ in range(n)]
dijkstra(door[0][0], door[0][1])
print(min(dp[door[1][1]][door[1][0]]))