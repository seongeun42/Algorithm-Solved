import sys, heapq
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dijkstra(y, x):
    hq = [(-1, x, y, -1)]
    heapq.heapify(hq)
    visit = [[0] * w for _ in range(h)]
    visit[y][x] += 1
    while hq:
        s_w, s_x, s_y, s_d = heapq.heappop(hq)
        if dp[s_y][s_x] < s_w:
            continue
        for i in range(4):
            n_x, n_y = s_x + dx[i], s_y + dy[i]
            if 0 <= n_x < w and 0 <= n_y < h and jido[n_y][n_x] != '*':
                n_w, n_d = s_w, s_d
                if s_d == -1 or s_d != i:
                    n_w += 1
                    n_d = i
                if visit[n_y][n_x] < 4 and n_w <= dp[n_y][n_x]:
                    dp[n_y][n_x] = n_w
                    heapq.heappush(hq, (n_w, n_x, n_y, n_d))
                visit[n_y][n_x] += 1

w, h = map(int, input().split())
jido = [input().strip() for _ in range(h)]
c = []
for i in range(h):
    for j in range(w):
        if jido[i][j] == 'C':
            c.append((i, j))
dp = [[1e9] * w for _ in range(h)]
dp[c[0][0]][c[0][1]] = -1
dijkstra(c[0][0], c[0][1])
print(dp[c[1][0]][c[1][1]])