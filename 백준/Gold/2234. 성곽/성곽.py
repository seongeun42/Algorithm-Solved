from collections import deque
import sys
input = sys.stdin.readline

dc = [-1, 0, 1, 0]
dr = [0, -1, 0, 1]

def bfs(N, M, rooms, visited, sr, sc, num):
    q = deque([(sr, sc)])
    visited[sr][sc] = num
    area = 0
    while q:
        cr, cc = q.popleft()
        area += 1
        for d in range(4):
            if rooms[cr][cc] & (1 << d) != 0:
                continue
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = num
                q.append((nr, nc))
    return area

def solve():
    N, M = map(int, input().split())
    rooms = [[*map(int, input().split())] for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    cnt, area, new_max_area = 0, [], 0
    for i in range(M):
        for j in range(N):
            if not visited[i][j]:
                area.append(bfs(N, M, rooms, visited, i, j, cnt + 1))
                cnt += 1
    for i in range(M):
        for j in range(N):
            for d in range(4):
                nr, nc = i + dr[d], j + dc[d]
                if 0 <= nr < M and 0 <= nc < N and visited[i][j] != visited[nr][nc]:
                    new_max_area = max(new_max_area, area[visited[i][j] - 1] + area[visited[nr][nc] - 1])
    print(cnt, max(area), new_max_area, sep="\n")

solve()