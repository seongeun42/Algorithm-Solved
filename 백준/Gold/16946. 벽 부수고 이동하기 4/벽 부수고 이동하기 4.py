from collections import deque
import sys
input = sys.stdin.readline

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs(N, M, arr, sr, sc, visited, num):
    q = deque([(sr, sc)])
    visited[sr][sc] = num
    cnt = 1
    while q:
        cr, cc = q.popleft()
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == '0' and visited[nr][nc] == -1:
                    visited[nr][nc] = num
                    cnt += 1
                    q.append((nr, nc))
    return cnt

def solve():
    N, M = map(int, input().split())
    arr = [input().rstrip() for _ in range(N)]
    cnt = []
    visited = [[-1] * M for _ in range(N)]
    ans = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '0' and visited[i][j] == -1:
                cnt.append(bfs(N, M, arr, i, j, visited, len(cnt)))
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '1':
                ans[i][j] = 1
                chk = set()
                for d in range(4):
                    nr, nc = i + dr[d], j + dc[d]
                    if 0 <= nr < N and 0 <= nc < M:
                        if arr[nr][nc] == '0' and visited[nr][nc] not in chk:
                            ans[i][j] += cnt[visited[nr][nc]]
                            chk.add(visited[nr][nc])
                ans[i][j] %= 10
    for v in ans:
        print("".join(map(str, v)))

solve()