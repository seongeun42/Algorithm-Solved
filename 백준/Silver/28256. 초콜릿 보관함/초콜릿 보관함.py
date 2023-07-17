import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    cnt = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 3 and 0 <= ny < 3:
            if not visited[ny][nx] and box[ny][nx] == 'O':
                visited[ny][nx] = 1
                cnt += dfs(nx, ny)
    return cnt

T = int(input())
for _ in range(T):
    box = [input().rstrip() for _ in range(3)]
    state = [*map(int, input().split())][1:]
    ans = []
    visited = [[0] * 3 for _ in range(3)]
    visited[1][1] = -1
    for i in range(3):
        for j in range(3):
            if not visited[i][j]:
                visited[i][j] = 1
                if box[i][j] == "O":
                    ans.append(dfs(j, i))
    print(1 if sorted(ans) == state else 0)