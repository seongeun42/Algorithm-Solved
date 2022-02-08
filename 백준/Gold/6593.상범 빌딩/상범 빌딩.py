import sys
from collections import deque


def getStart(building, L, R, C):
    for l in range(L):
        for r in range(R):
            for c in range(C):
                if building[l][r][c] == "S":
                    return [c, r, l]
    return -1


def solve(building, L, R, C, start):
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

    q = deque()
    q.append([start[0], start[1], start[2], 0])
    visited[start[2]][start[1]][start[0]] = True
    while q:
        x, y, f, count = q.popleft()

        if building[f][y][x] == "E":
            return count

        for i in range(4):
            nxt_x, nxt_y = x + dx[i], y + dy[i]
            if not (0 <= nxt_x < C and 0 <= nxt_y < R):
                continue
            if building[f][nxt_y][nxt_x] == "#":
                continue
            if visited[f][nxt_y][nxt_x]:
                continue
            visited[f][nxt_y][nxt_x] = True
            q.append([nxt_x, nxt_y, f, count + 1])

        for v in [-1, 1]:
            if not (0 <= f + v < L):
                continue
            if building[f + v][y][x] == "#":
                continue
            if visited[f + v][y][x]:
                continue
            visited[f + v][y][x] = True
            q.append([x, y, f + v, count + 1])
    return 0


input = sys.stdin.readline
while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    building = []
    for i in range(L):
        building.append([input() for _ in range(R)])
        input()

    start = getStart(building, L, R, C)
    elapsed = solve(building, L, R, C, start)
    print("Trapped!" if elapsed == 0 else f"Escaped in {elapsed} minute(s).")
