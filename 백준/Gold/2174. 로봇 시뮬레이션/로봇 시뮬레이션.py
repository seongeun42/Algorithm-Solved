import sys
input = sys.stdin.readline

dir = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

# N, E, S, W
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def turn(c, rb, cnt):
    cnt %= 4
    if c == 'L':
        cnt *= -1
    robot[rb][2] = (robot[rb][2] + cnt) % 4

def move(rb, cnt):
    nx, ny, d = robot[rb]
    for i in range(cnt):
        nx += dx[d]
        ny += dy[d]
        if not (0 <= nx < A and 0 <= ny < B):
            return -1
        if ground[ny][nx] != 0:
            return ground[ny][nx]
    ground[robot[rb][1]][robot[rb][0]] = 0
    ground[ny][nx] = rb + 1
    robot[rb] = [nx, ny, d]
    return 0

def simul():
    for r, c, cnt in cmd:
        if c == 'F':
            res = move(r, cnt)
            if res == -1:
                return f"Robot {r + 1} crashes into the wall"
            if res > 0:
                return f"Robot {r + 1} crashes into robot {res}"
        else:
            turn(c, r, cnt)
    return "OK"

A, B = map(int, input().split())
N, M = map(int, input().split())
ground = [[0] * A for _ in range(B)]
robot = []
for i in range(N):
    x, y, d = input().split()
    robot.append([int(x) - 1, B - int(y), dir[d]])
    ground[robot[-1][1]][robot[-1][0]] = i + 1
cmd = []
for _ in range(M):
    r, c, cnt = input().split()
    cmd.append((int(r) - 1, c, int(cnt)))
    
print(simul())