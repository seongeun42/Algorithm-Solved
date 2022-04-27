from _collections import deque

def bfs(sr, sc, er, ec):
    q = deque([(sr, sc)])
    visited[sr][sc] = 0
    while q:
        r, c = q.popleft()
        if r == er and c == ec:
            return visited[er][ec]
        for i in range(6):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
    return -1

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]
visited = [[-1] * N for _ in range(N)]
print(bfs(r1, c1, r2, c2))