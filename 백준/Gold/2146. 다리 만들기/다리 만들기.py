from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 육지 분류
def dfs(cx, cy, sea, n):
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if 0 <= nx < len(sea) and 0 <= ny < len(sea) and sea[ny][nx] == 1:
            sea[ny][nx] = n
            dfs(nx, ny, sea, n)

# 대륙 간 거리 구하기
def bfs(sea, n):
    q = deque([])
    for i in range(len(sea)):
        for j in range(len(sea)):
            if sea[i][j] == n:
                q.append((i,j))
    visited = [[0] * len(sea) for _ in range(len(sea))]
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= nx < len(sea) and 0 <= ny < len(sea) and visited[ny][nx] == 0 and sea[ny][nx] != n:
                # 바다라면 거리 +1
                if sea[ny][nx] == 0:
                    visited[ny][nx] = visited[cy][cx] + 1
                    q.append((ny, nx))
                else:
                    # 다른 대륙이라면 거리 반환
                    return visited[cy][cx]
    return -1

def solve():
    N = int(input())
    sea = [[*map(int, input().split())] for _ in range(N)]
    # 대륙 구분하기
    cnt = 2
    for i in range(N):
        for j in range(N):
            if sea[i][j] == 1:
                sea[i][j] = cnt
                dfs(j, i, sea, cnt)
                cnt += 1
    # 대륙 간 거리 구하기
    ans = 10000
    for k in range(2, cnt):
        dist = bfs(sea, k)
        if dist != -1 and ans > dist:
            ans = dist
    print(ans)

solve()