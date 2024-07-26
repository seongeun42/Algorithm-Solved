import sys, heapq
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    circuit = [input().rstrip() for _ in range(N)]
    dp = [[1e9] * M for _ in range(N)]
    dp[0][0] = 0 if circuit[0][0] == '\\' else 1
    dir = {'\\': [(-1, -1, '\\'), (1, 1, '\\'), (-1, 0, '/'),
                  (0, -1, '/'), (0, 1, '/'), (1, 0, '/')],
            '/': [(-1, 1, '/'), (1, -1, '/'), (-1, 0, '\\'),
                  (0, -1, '\\'), (0, 1, '\\'), (1, 0, '\\')]}
    hq = []
    heapq.heappush(hq, (dp[0][0], 0, 0, '\\'))
    while hq:
        cw, cr, cc, state = heapq.heappop(hq)
        if dp[cr][cc] < cw:
            continue
        for dr, dc, ds in dir[state]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < M:
                if nr == N - 1 and nc == M - 1 and ds == '/':
                    continue
                nw = 0 if circuit[nr][nc] == ds else 1
                if cw + nw < dp[nr][nc]:
                    dp[nr][nc] = cw + nw
                    heapq.heappush(hq, (cw + nw, nr, nc, ds))
    print(dp[-1][-1] if dp[-1][-1] != 1e9 else "NO SOLUTION")

solve()