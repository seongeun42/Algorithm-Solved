import sys
input = sys.stdin.readline

def dfs(r, c, flag):
    visit[r][c] = 1
    for i in range(8):
        a, b = c + dx[i], r + dy[i]
        if 0 <= a < M and 0 <= b < N:
            if mt[b][a] > mt[r][c]:
                flag = 0
            if not visit[b][a] and mt[b][a] == mt[r][c]:
                flag = min(flag, dfs(b, a, flag))
    return flag

N, M = map(int, input().split())
mt = [[*map(int, input().split())] for _ in range(N)]
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]
visit = [[0] * M for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if mt[i][j] > 0 and not visit[i][j]:
            cnt += 1 if dfs(i, j, 1) else 0
print(cnt)