import sys, heapq
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    forest = [input().rstrip() for _ in range(N)]
    tree = []
    hw, home = [], []
    for i in range(N):
        for j in range(M):
            if forest[i][j] == '+':
                tree.append((i, j))
            elif forest[i][j] == 'V':
                hw = (i, j)
            elif forest[i][j] == 'J':
                home = (i, j)

    dr, dc = [0, 1, 0, -1], [-1, 0, 1, 0]
    
    # 각 칸의 가장 가까운 나무와의 거리 구하기
    t_dist = [[1001] * M for _ in range(N)]
    hq = []
    for a, b in tree:
        heapq.heappush(hq, (0, a, b))
        t_dist[a][b] = 0
    while hq:
        cw, cr, cc = heapq.heappop(hq)
        if t_dist[cr][cc] < cw:
            continue
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                w = cw + (abs(nr - cr) + abs(nc - cc))
                if w < t_dist[nr][nc]:
                    t_dist[nr][nc] = w
                    heapq.heappush(hq, (w, nr, nc))

    # 가장 안전한 길 탐색
    # 다음 칸의 나무 거리, 경로 상의 최소 거리, r, c 
    hq = [(-t_dist[hw[0]][hw[1]], t_dist[hw[0]][hw[1]], hw[0], hw[1])]
    visited = [[False] * M for _ in range(N)]
    visited[hw[0]][hw[1]] = True
    ans = t_dist[hw[0]][hw[1]]
    while hq:
        cw, min_dist, cr, cc = heapq.heappop(hq)
        if (cr, cc) == home:
            ans = min_dist
            break
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                visited[nr][nc] = True
                heapq.heappush(hq, (-t_dist[nr][nc], min(min_dist, t_dist[nr][nc]), nr, nc))
    print(ans)

solve()