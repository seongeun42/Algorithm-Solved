import sys, heapq
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    q = []
    heapq.heappush(q, (m[0][0], 0, 0))
    while q:
        s_w, sy, sx = heapq.heappop(q)
        if dp[sy][sx] < s_w:
            continue
        for i in range(4):
            ny, nx = sy + dy[i], sx + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if m[ny][nx] + s_w < dp[ny][nx]:
                    dp[ny][nx] = m[ny][nx] + s_w
                    heapq.heappush(q, (dp[ny][nx], ny, nx))

i = 1
while 1:
    n = int(input())
    if n == 0: break
    m = [[*map(int, input().split())] for _ in range(n)]
    dp = [[1e9] * n for _ in range(n)]
    dp[0][0] = m[0][0]
    dijkstra()
    print(f'Problem {i}: {dp[-1][-1]}')
    i += 1