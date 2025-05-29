from collections import deque
import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def bfs(arr, start, edges, N, M, ids):
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    q = deque([start])
    visited = [[0] * N for _ in range(N)]
    visited[start[0]][start[1]] = 1
    cnt = 0
    while q:
        cr, cc = q.popleft()
        if (cr, cc) != start and arr[cr][cc] in {'S', 'K'}:
            edges.append((visited[cr][cc] - 1, ids[start], ids[(cr, cc)]))
            cnt += 1
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] != '1':
                visited[nr][nc] = visited[cr][cc] + 1
                q.append((nr, nc))
    return cnt == M

def solve():
    N, M = map(int, input().split())
    arr = [input().rstrip() for _ in range(N)]
    ids = {}
    edges = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] in {'S', 'K'}:
                ids[(i, j)] = len(ids)
    for start in ids.keys():
        if not bfs(arr, start, edges, N, M, ids):
            print(-1)
            return
    R = list(range(len(ids)))
    edges.sort()
    ans = 0
    for dist, u, v in edges:
        ur = find_root(u, R)
        vr = find_root(v, R)
        if ur != vr:
            R[max(ur, vr)] = min(ur, vr)
            ans += dist
    print(ans)

solve()