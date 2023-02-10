from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
play = [[0] * N for _ in range(N)]
play[0][0] = -1
for _ in range(K):
    ar, ac = map(int, input().split())
    play[ar - 1][ac - 1] = 1
dc = [1, 0, -1, 0]
dr = [0, 1, 0, -1]
L = int(input())
move = [input().split() for _ in range(L)]
snake = deque([[0, 0]])
moveDir = 0
ptime = 0
stop = False
for i in range(L + 1):
    if i == L:
        X, C = ptime + N, move[-1][1]
    else:
        X, C = move[i]
    for i in range(int(X) - ptime):
        ptime += 1
        nr, nc = snake[0][0] + dr[moveDir], snake[0][1] + dc[moveDir]
        if 0 <= nr < N and 0 <= nc < N and play[nr][nc] != -1:
            snake.appendleft([nr, nc])
            if play[nr][nc] == 0 and len(snake) != 1:
                tr, tc = snake.pop()
                play[tr][tc] = 0
            play[nr][nc] = -1
        else:
            stop = True
            break
    if stop:
        break
    if C == "L":
        moveDir = (moveDir - 1) % 4
    else:
        moveDir = (moveDir + 1) % 4
print(ptime)