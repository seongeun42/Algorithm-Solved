from collections import deque

def bfs(x, y):
    q = deque([[x, y]])
    B[y][x] = 0
    while q:
        v = q.popleft()
        for i in range(4):
            a, b = v[0] + dx[i], v[1] + dy[i]
            if not (0 <= a < w and 0 <= b < h):
                return B[v[1]][v[0]] + 1
            if B[b][a] != '#' and B[b][a] != '.':
                if B[v[1]][v[0]] + 1 < -B[b][a]:
                    B[b][a] = B[v[1]][v[0]] + 1
                    q.append([a, b])
            if B[b][a] == '.':
                B[b][a] = B[v[1]][v[0]] + 1
                q.append([a, b])
    return "IMPOSSIBLE"

def fire_bfs():
    while fire:
        v = fire.popleft()
        for i in range(4):
            a, b = v[0] + dx[i], v[1] + dy[i]
            if 0 <= a < w and 0 <= b < h:
                if B[b][a] == '.' or B[b][a] == '@':
                    B[b][a] = B[v[1]][v[0]] - 1
                    fire.append([a, b])

T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    B = [list(input()) for _ in range(h)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    fire = deque([])
    sg = []
    for i in range(h):
        for j in range(w):
            if B[i][j] == '*':
                fire.append([j, i])
                B[i][j] = 0
            if B[i][j] == '@':
                sg = [j, i]
                B[i][j] = 0
    fire_bfs()
    print(bfs(sg[0], sg[1]))