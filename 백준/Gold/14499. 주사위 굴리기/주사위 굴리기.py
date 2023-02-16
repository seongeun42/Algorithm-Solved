import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
jido = [[*map(int, input().split())] for _ in range(N)]
op = [*map(int, input().split())]

# 동서북남
dc = [1, -1, 0, 0]
dr = [0, 0, -1, 1]

# 주사위
dice = [0] * 6
loca = [x, y]
top, bottom = 1, 6
sideE, sideW = 3, 4
sideN, sideS = 2, 5

for o in op:
    nx = loca[0] + dr[o - 1]
    ny = loca[1] + dc[o - 1]
    if 0 <= nx < N and 0 <= ny < M:
        if o == 1:
            top, bottom, sideE, sideW = sideE, sideW, bottom, top
        elif o == 2:
            top, bottom, sideE, sideW = sideW, sideE, top, bottom
        elif o == 3:
            top, bottom, sideN, sideS = sideN, sideS, bottom, top
        else:
            top, bottom, sideN, sideS = sideS, sideN, top, bottom

        if jido[nx][ny]:
            dice[bottom - 1] = jido[nx][ny]
            jido[nx][ny] = 0
        else:
            jido[nx][ny] = dice[bottom - 1]
            
        print(dice[top - 1])
        loca = [nx, ny]