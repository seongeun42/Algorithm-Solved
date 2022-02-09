from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visit = [[[0] * 2 for i in range(M)] for i in range(N)]
    q = deque([[0, 0, 0]])
    visit[0][0] = [1, 1]
    while q:
        x, y, f = q.popleft()
        if [x, y] == [M - 1, N - 1]:
            return visit[y][x][f]
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if 0 <= a < M and 0 <= b < N:
                if mp[b][a] == 0 and visit[b][a][f] == 0:
                    visit[b][a][f] = visit[y][x][f] + 1
                    q.append([a, b, f])
                if mp[b][a] == 1 and f == 0:
                    visit[b][a][1] = visit[y][x][f] + 1
                    q.append([a, b, 1])
    return -1

N, M = map(int, input().split())
mp = [[*map(int, list(input().rstrip()))] for _ in range(N)]
print(bfs())