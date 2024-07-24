import sys, heapq
input = sys.stdin.readline

def solve():
    N, M, T, D = map(int, input().split())
    mountain = [[] for _ in range(N)]
    alpa = {chr(65 + i): i for i in range(26)}
    alpa.update({chr(97 + i): i + 26 for i in range(26)})
    for i in range(N):
        S = input().rstrip()
        for c in S:
            mountain[i].append(alpa[c])
    dr = [1, 0, -1, 0]
    dc = [0, -1, 0, 1]
    up = [[1e9] * M for _ in range(N)]
    down = [[1e9] * M for _ in range(N)]
    up[0][0] = 0
    down[0][0] = 0
    hq = []
    heapq.heappush(hq, (0, 0, 0))
    while hq:
        cw, cr, cc = heapq.heappop(hq)
        if up[cr][cc] < cw:
            continue
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M and abs(mountain[cr][cc] - mountain[nr][nc]) <= T:
                nw = 1 if mountain[cr][cc] >= mountain[nr][nc] else (mountain[cr][cc] - mountain[nr][nc]) ** 2
                if cw + nw < up[nr][nc]:
                    up[nr][nc] = cw + nw
                    heapq.heappush(hq, (cw + nw, nr, nc))
    heapq.heappush(hq, (0, 0, 0))
    while hq:
        cw, cr, cc = heapq.heappop(hq)
        if down[cr][cc] < cw:
            continue
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M and abs(mountain[cr][cc] - mountain[nr][nc]) <= T:
                nw = 1 if mountain[cr][cc] <= mountain[nr][nc] else (mountain[cr][cc] - mountain[nr][nc]) ** 2
                if cw + nw < down[nr][nc]:
                    down[nr][nc] = cw + nw
                    heapq.heappush(hq, (cw + nw, nr, nc))
    ans = 0
    for i in range(N):
        for j in range(M):
            if up[i][j] + down[i][j] <= D and ans < mountain[i][j]:
                ans = mountain[i][j]
    print(ans)

solve()