import sys, heapq
input = sys.stdin.readline

def dijkstra():
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    hq = []
    heapq.heappush(hq, (0, S[0], S[1]))
    while hq:
        cw, cr, cc = heapq.heappop(hq)
        if dp[cr][cc] < cw:
            continue
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                nw = 0
                if forest[nr][nc] == '.':
                    for i in range(4):
                        nnr, nnc = nr + dr[i], nc + dc[i]
                        if 0 <= nnr < N and 0 <= nnc < M and forest[nnr][nnc] == 'g':
                            nw = 1
                            break
                elif forest[nr][nc] == 'g':
                    nw = 10000
                if cw + nw < dp[nr][nc]:
                    dp[nr][nc] = cw + nw
                    heapq.heappush(hq, (cw + nw, nr, nc))

N, M = map(int, input().split())
forest = [input().rstrip() for _ in range(N)]
S, F = None, None
for i in range(N):
    for j in range(M):
        if forest[i][j] == 'S':
            S = [i, j]
        if forest[i][j] == 'F':
            F = [i, j]
dp = [[1e9] * M for _ in range(N)]
dp[S[0]][S[1]] = 0
dijkstra()
print(*divmod(dp[F[0]][F[1]], 10000))