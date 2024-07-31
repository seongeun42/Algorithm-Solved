from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def find_root(rc, root):
    if root[rc[0]][rc[1]] != rc:
        root[rc[0]][rc[1]] = find_root(root[rc[0]][rc[1]], root)
    return root[rc[0]][rc[1]]

def union(one, two, root):
    ro = find_root(one, root)
    rt = find_root(two, root)
    if ro == rt:
        return
    # 왼쪽상단으로 통일
    if ro[0] < rt[0]:
        root[rt[0]][rt[1]] = ro
    elif ro[0] == rt[0]:
        if ro[1] < rt[1]:
            root[rt[0]][rt[1]] = ro
        else:
            root[ro[0]][ro[1]] = rt
    else:
        root[ro[0]][ro[1]] = rt

def init(lake, root):
    R, C = len(lake), len(lake[0])
    visited = [[0] * C for _ in range(R)]
    edge = []
    for i in range(R):
        for j in range(C):
            if lake[i][j] == 'X' or visited[i][j]:
                continue
            q = deque([(i, j)])
            visited[i][j] = 1
            while q:
                cr, cc = q.popleft()
                for d in range(4):
                    nr, nc = cr + dr[d], cc + dc[d]
                    if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                        visited[nr][nc] = 1
                        if lake[nr][nc] != 'X':
                            root[nr][nc] = (i, j)
                            q.append((nr, nc))
                        else:
                            edge.append((cr, cc))
    return edge

def solve():
    R, C = map(int, input().split())
    lake = [list(input().rstrip()) for _ in range(R)]
    root = [[] for _ in range(R)]
    swan = []
    for i in range(R):
        for j in range(C):
            root[i].append((i, j))
            if lake[i][j] == 'L':
                swan.append((i, j))
    # root 초기화 & 첫날 녹는 빙판 배열
    edge = init(lake, root)
    # 빙판 녹기
    ans = 0
    visited = [[0] * C for _ in range(R)]
    edge = deque(edge)
    while edge and find_root(swan[0], root) != find_root(swan[1], root):
        ans += 1
        next_edge = deque([])
        while edge:
            cr, cc = edge.popleft()
            for d in range(4):
                nr, nc = cr + dr[d], cc + dc[d]
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and lake[nr][nc] == 'X':
                    visited[nr][nc] = 1
                    lake[nr][nc] = '.'
                    root[nr][nc] = root[cr][cc]
                    for dd in range(4):
                        nnr, nnc = nr + dr[dd], nc + dc[dd]
                        # 근처가 호수면 합치기
                        if 0 <= nnr < R and 0 <= nnc < C and lake[nnr][nnc] != 'X':
                            union((nr, nc), (nnr, nnc), root)
                    next_edge.append((nr, nc))
        edge = next_edge
    print(ans)

solve()