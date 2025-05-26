import sys
input = sys.stdin.readline

def find_root(rc, R):
    if R[rc[0]][rc[1]] != rc:
        R[rc[0]][rc[1]] = find_root(R[rc[0]][rc[1]], R)
    return R[rc[0]][rc[1]]

def solve():
    N, M = map(int, input().split())
    maze = [list(input().rstrip()) for _ in range(N)]
    move = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    R = []
    for i in range(N):
        R.append([])
        for j in range(M):
            R[i].append((i, j))
    out = [[False] * M for _ in range(N)]
    cnt = [[1] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            curR = find_root((i, j), R)
            d = move[maze[i][j]]
            if 0 <= i + d[0] < N and 0 <= j + d[1] < M:
                nxt = (i + d[0], j + d[1])
                nxtR = find_root(nxt, R)
                if curR != nxtR:
                    if curR[0] * M + curR[1] <= nxtR[0] * M + nxtR[1]:
                        if out[nxtR[0]][nxtR[1]]:
                            out[curR[0]][curR[1]] = True
                        cnt[curR[0]][curR[1]] += cnt[nxtR[0]][nxtR[1]]
                        R[nxtR[0]][nxtR[1]] = curR
                    else:
                        if out[curR[0]][curR[1]]:
                            out[nxtR[0]][nxtR[1]] = True
                        cnt[nxtR[0]][nxtR[1]] += cnt[curR[0]][curR[1]]
                        R[curR[0]][curR[1]] = nxtR
            else:
                out[curR[0]][curR[1]] = True
    ans = 0
    for i in range(N):
        for j in range(M):
            r, c = find_root((i, j), R)
            if R[r][c] == (i, j) and out[r][c]:
                ans += cnt[r][c]
    print(ans)

solve()