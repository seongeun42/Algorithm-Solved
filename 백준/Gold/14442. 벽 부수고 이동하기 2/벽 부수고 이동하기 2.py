from collections import deque
import sys
input = sys.stdin.readline

def bfs(N, M, K, matr):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[[0] * (M) for _ in range(N)] for _ in range(K + 1)]
    visited[0][0][0] = 1
    q = deque([(0, 0, 0)])
    while q:
        cx, cy, cnt = q.popleft()
        if cx == M - 1 and cy == N - 1:
            return visited[cnt][cy][cx]
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if visited[cnt][ny][nx] == 0 and matr[ny][nx] == "0":
                    visited[cnt][ny][nx] = visited[cnt][cy][cx] + 1
                    q.append((nx, ny, cnt))
                elif cnt < K and visited[cnt + 1][ny][nx] == 0:
                    visited[cnt + 1][ny][nx] = visited[cnt][cy][cx] + 1
                    q.append((nx, ny, cnt + 1))
    return -1

def solve():
    N, M, K = map(int, input().split())
    matr = [input().rstrip() for _ in range(N)]
    print(bfs(N, M, K, matr))

solve()