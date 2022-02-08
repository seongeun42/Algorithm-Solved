from collections import deque
import sys
input = sys.stdin.readline

def bfs(s, e):
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    q = deque([s])
    B[s[0]][s[1]][s[2]] = 1
    while q:
        v = q.popleft()
        if v == e:
            print("Escaped in", B[e[0]][e[1]][e[2]] - 1, "minute(s).")
            return
        for i in range(6):
            x, y, z = v[2] + dx[i], v[1] + dy[i], v[0] + dz[i]
            if 0 <= x < C and 0 <= y < R and 0 <= z < L:
                if not B[z][y][x]:
                    B[z][y][x] = B[v[0]][v[1]][v[2]] + 1
                    q.append([z, y, x])
    print("Trapped!")

while 1:
    L, R, C = map(int, input().split())
    S, E = [], []
    if L == R == C == 0:
        break
    B = []
    for f in range(L):
        B.append([])
        for i in range(R):
            B[f].append([])
            a = list(input().rstrip())
            for j, v in enumerate(a):
                if v == '.':
                    B[f][i].append(0)
                elif v == '#':
                    B[f][i].append(1)
                elif v == 'S':
                    S = [f, i, j]
                    B[f][i].append(0)
                else:
                    E = [f, i, j]
                    B[f][i].append(0)
        input()
    bfs(S, E)