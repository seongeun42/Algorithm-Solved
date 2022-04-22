import sys
input = sys.stdin.readline

def setting():
    for i in range(R):
        for j in range(C):
            if pan[i][j] == '.':
                pan[i][j] = 'O'

def bomb_coordi():
    bomb = []
    for i in range(R):
        for j in range(C):
            if pan[i][j] == 'O':
                bomb.append((i, j))
    return bomb

R, C, N = map(int, input().split())
pan = [list(input().strip()) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
bomb = bomb_coordi()

for i in range(2, N + 1):
    if i % 2 == 0:
        setting()
    else:
        for r, c in bomb:
            pan[r][c] = '.'
            for d in range(4):
                a, b = r + dy[d], c + dx[d]
                if 0 <= a < R and 0 <= b < C:
                    pan[a][b] = '.'
        bomb = bomb_coordi()

for s in pan:
    print(''.join(s))