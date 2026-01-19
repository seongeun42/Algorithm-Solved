from collections import deque
import sys
input = sys.stdin.readline

def bfs(arr, x, y, visited, num):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    q = deque([(x, y)])
    visited[x][y] = num
    while q:
        cx, cy = q.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 < nx < len(arr) and 0 < ny < len(arr[0]):
                if arr[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = num
                    q.append((nx, ny))

def solve():
    N, M, K = map(int, input().split())
    # 밤하늘 표시
    arr = [[True] * (M + 1) for _ in range(N + 1)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[x][y] = False
    # 전체에서 같은 길 표시
    path = [[0] * (M + 1) for _ in range(N + 1)]
    path_cnt = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if arr[i][j] and not path[i][j]:
                path_cnt += 1
                bfs(arr, i, j, path, path_cnt)
    # 범위 내 특정 길 시작점 개수 세기
    ab = [[*map(int, input().split())] for _ in range(4)]
    me = [0] * (path_cnt + 1)
    for i in range(ab[0][0], ab[1][0] + 1):
        for j in range(ab[0][1], ab[1][1] + 1):
            if path[i][j] > 0:
                me[path[i][j]] += 1
    you = [0] * (path_cnt + 1)
    for i in range(ab[2][0], ab[3][0] + 1):
        for j in range(ab[2][1], ab[3][1] + 1):
            if path[i][j] > 0:
                you[path[i][j]] += 1
    # 조합 개수 세기
    ans = 0
    for i in range(path_cnt + 1):
        ans += me[i] * you[i]
    print(ans)

solve()