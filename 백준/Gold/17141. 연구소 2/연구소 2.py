from collections import deque
import sys
input = sys.stdin.readline
        
def bfs(choose_virus, empty):
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    empty -= len(choose_virus)
    q = deque(choose_virus)
    visited = [[-1] * N for _ in range(N)]
    for r, c in choose_virus:
        visited[r][c] = 0
    time = 0
    while q:
        cr, cc = q.popleft()
        for d in range(4):
            nr, nc = cr + dy[d], cc + dx[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1 and lab[nr][nc] != 1:
                visited[nr][nc] = visited[cr][cc] + 1
                empty -= 1
                if visited[nr][nc] > time:
                    time = visited[nr][nc]
                q.append((nr, nc))
    return time if empty == 0 else -1

def combination(cur, dep, max_cnt, arr):
    global ans
    if dep == max_cnt:
        time = bfs(arr, empty_cnt)
        if time != -1 and time < ans:
            ans = time
        return
    for i in range(cur + 1, len(virus)):
        arr.append(virus[i])
        combination(i, dep + 1, max_cnt, arr)
        arr.pop()

N, M = map(int, input().split())
lab = [[*map(int, input().split())] for _ in range(N)]
virus = []
empty_cnt = 0
ans = 1e9
for i in range(N):
    for j in range(N):
        if lab[i][j] == 1:
            continue
        if lab[i][j] == 2:
            virus.append((i, j))
        empty_cnt += 1
combination(-1, 0, M, [])
print(ans if ans != 1e9 else -1)