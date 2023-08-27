from collections import deque
import sys
input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(baby, babySize, sea, N):
    q = deque([baby])
    visit = [[-1] * N for _ in range(N)]
    visit[baby[0]][baby[1]] = 0
    dist = 1
    while q:
        qSize = len(q)
        prey = []
        for _ in range(qSize):
            cy, cx = q.popleft()
            for d in range(4):
                ny, nx = cy + dy[d], cx + dx[d]
                if 0 <= ny < N and 0 <= nx < N and visit[ny][nx] == -1 and sea[ny][nx] <= babySize:
                    visit[ny][nx] = visit[cy][cx] + 1
                    q.append([ny, nx])
                    if sea[ny][nx] != 0 and sea[ny][nx] < babySize:
                        prey.append([ny, nx])
        if len(prey) != 0:
            prey.sort(key=lambda x: [x[0], x[1]])
            return prey[0], dist
        dist += 1
    return False, -1


def solve():
    N = int(input())
    sea = [[0] * N for _ in range(N)]
    baby = []
    fish = 0
    for i in range(N):
        line = [*map(int, input().split())]
        for j in range(N):
            if line[j] == 9:
                baby = [i, j]
            elif line[j] != 0:
                sea[i][j] = line[j]
                fish += 1
    babySize = 2
    eat = 0
    time = 0
    while fish:
        target, dist = bfs(baby, babySize, sea, N)
        if target == False:
            break
        baby = target
        sea[target[0]][target[1]] = 0
        fish -= 1
        eat += 1
        if eat == babySize:
            eat = 0
            babySize += 1
        time += dist
    print(time)

solve()