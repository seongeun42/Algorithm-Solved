from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque([hed])
    forest[hed[1]][hed[0]] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if [a, b] == bea:
                return forest[y][x]
            if 0 <= a < C and 0 <= b < R and not forest[b][a]:
                if forest[y][x] + 1 < time[b][a]:
                    forest[b][a] = forest[y][x] + 1
                    q.append([a, b])
    return "KAKTUS"

def flood():
    while water:
        x, y = water.popleft()
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if 0 <= a < C and 0 <= b < R:
                if not forest[b][a] and time[b][a] == 2500:
                    time[b][a] = time[y][x] + 1
                    water.append([a, b])

R, C = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
forest = [list(input().strip()) for _ in range(R)]
time = [[2500] * C for _ in range(R)]
water = deque([])
hed, bea = [], []
for i in range(R):
    for j in range(C):
        if forest[i][j] == '.':
            forest[i][j] = 0
        elif forest[i][j] == 'X':
            forest[i][j] = 1
        elif forest[i][j] == '*':
            forest[i][j] = 1
            time[i][j] = 1
            water.append([j, i])
        elif forest[i][j] == 'S':
            forest[i][j] = 0
            hed = [j, i]
        elif forest[i][j] == 'D':
            forest[i][j] = -1
            bea = [j, i]
flood()
print(bfs())