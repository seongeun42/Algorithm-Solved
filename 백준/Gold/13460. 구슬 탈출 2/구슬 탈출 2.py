from collections import deque

# 왼오위아
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, dx, dy):
    cnt = 0
    while board[y + dy][x + dx] != "#" and board[y][x] != "O":
        y += dy
        x += dx
        cnt += 1
    return x, y, cnt

def bfs(rx, ry, bx, by):
    q = deque([[rx, ry, bx, by, 1]])
    visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visited[ry][rx][by][bx] = 1
    while q:
        crx, cry, cbx, cby, ccnt = q.popleft()
        if ccnt > 10:
            break
        for i in range(4):
            nrx, nry, rmove = move(crx, cry, dx[i], dy[i])
            nbx, nby, bmove = move(cbx, cby, dx[i], dy[i])
            if board[nby][nbx] != 'O':
                if board[nry][nrx] == 'O':
                    return ccnt
                if [nry, nrx] == [nby, nbx]:
                    if rmove > bmove:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nry][nrx][nby][nbx]:
                    visited[nry][nrx][nby][nbx] = 1
                    q.append([nrx, nry, nbx, nby, ccnt + 1])
    return -1

n, m = map(int, input().split())
board = []
rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    l = input()
    if "B" in l:
        by, bx = i, l.find("B")
    if "R" in l:
        ry, rx = i, l.find("R")
    board.append(list(l))

print(bfs(rx, ry, bx, by))