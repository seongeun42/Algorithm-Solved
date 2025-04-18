from collections import deque
import sys
input = sys.stdin.readline

def bfs(sr, sc, grass, road):
    q = deque([(sr, sc)])
    cow = grass[sr][sc]
    grass[sr][sc] = -1
    while q:
        cr, cc = q.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < len(grass) and 0 <= nc < len(grass) and grass[nr][nc] >= 0:
                if (cr, cc) in road and (nr, nc) in road[(cr, cc)]:
                    continue
                if (nr, nc) in road and (cr, cc) in road[(nr, nc)]:
                    continue
                cow += grass[nr][nc]
                grass[nr][nc] = -1
                q.append((nr, nc))
    return cow

def solve():
    N, K, R = map(int, input().split())
    grass = [[0] * N for _ in range(N)]
    road = {}
    for _ in range(R):
        r1, c1, r2, c2 = map(int, input().split())
        r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
        if (r1, c1) in road:
            road[(r1, c1)].add((r2, c2))
        else:
            road[(r1, c1)] = {(r2, c2)}
    for _ in range(K):
        r, c = map(int, input().split())
        grass[r - 1][c - 1] = 1
    cow_group = []
    for i in range(N):
        for j in range(N):
            if grass[i][j] >= 0:
                cnt = bfs(i, j, grass, road)
                if cnt > 0:
                    cow_group.append(cnt)
    ans = 0
    prefix = [cow_group[0]]
    for i in range(1, len(cow_group)):
        prefix.append(cow_group[i] + prefix[i - 1])
    for i, v in enumerate(cow_group):
        ans += v * (prefix[-1] - prefix[i])
    print(ans)

solve()