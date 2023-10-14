from collections import deque
import copy

# 우, 좌, 상, 하
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


# 벽 있는지 여부 확인
def exist_wall(r, c, d):
    # 우
    if d == 0 and (r, c) in wall and 1 in wall[(r, c)]:
        return True
    # 좌
    if d == 1 and (r, c - 1) in wall and 1 in wall[(r, c - 1)]:
        return True
    # 상
    if d == 2 and (r, c) in wall and 0 in wall[(r, c)]:
        return True
    # 하
    if d == 3 and (r + 1, c) in wall and 0 in wall[(r + 1, c)]:
        return True
    return False


# 온풍기 오른쪽
def right(r, c, t, visit, q):
    # 우
    if 0 <= c + 1 < C:
        nr, nc = r, c + 1
        # 사이에 벽이 없고, 같은 온풍기 바람이 아직 안 왔으면
        if not exist_wall(r, c, 0) and not visit[nr][nc]:
            temperate[nr][nc] += t
            visit[nr][nc] = True
            q.append((nr, nc))
    # 우상
    if 0 <= r - 1 < R and 0 <= c + 1 < C:
        nr, nc = r - 1, c + 1
        if not exist_wall(r, c, 2) and not exist_wall(r - 1, c, 0) and not visit[nr][nc]:
            temperate[nr][nc] += t
            visit[nr][nc] = True
            q.append((nr, nc))
    #우하
    if 0 <= r + 1 < R and 0 <= c + 1 < C:
        nr, nc = r + 1, c + 1
        if not exist_wall(r, c, 3) and not exist_wall(r + 1, c, 0) and not visit[nr][nc]:
            temperate[nr][nc] += t
            visit[nr][nc] = True
            q.append((nr, nc))


# 온풍기 왼쪽
def left(r, c, t, visit, q):
    # 좌
    if 0 <= c - 1 < C:
        nr, nc = r, c - 1
        # 사이에 벽이 없고, 같은 온풍기 바람이 아직 안 왔으면
        if not exist_wall(r, c, 1) and not visit[nr][nc]:
            temperate[nr][nc] += t
            visit[nr][nc] = True
            q.append((nr, nc))
    # 좌상
    if 0 <= r - 1 < R and 0 <= c - 1 < C:
        nr, nc = r - 1, c - 1
        if not exist_wall(r, c, 2) and not exist_wall(r - 1, c, 1) and not visit[nr][nc]:
            temperate[nr][nc] += t
            visit[nr][nc] = True
            q.append((nr, nc))
    #좌하
    if 0 <= r + 1 < R and 0 <= c - 1 < C:
        nr, nc = r + 1, c - 1
        if not exist_wall(r, c, 3) and not exist_wall(r + 1, c, 1) and not visit[nr][nc]:
            temperate[nr][nc] += t
            visit[nr][nc] = True
            q.append((nr, nc))


# 온풍기 위쪽
def up(r, c, t, visit, q):
    # 상
    if 0 <= r - 1 < R:
        nr, nc = r - 1, c
        # 사이에 벽이 없고, 같은 온풍기 바람이 아직 안 왔으면
        if not exist_wall(r, c, 2) and not visit[nr][nc]:
            temperate[nr][nc] += t
            visit[nr][nc] = True
            q.append((nr, nc))
    # 상좌
    if 0 <= r - 1 < R and 0 <= c - 1 < C:
        nr, nc = r - 1, c - 1
        if not exist_wall(r, c, 1) and not exist_wall(r, c - 1, 2) and not visit[nr][nc]:
            temperate[nr][nc] += t
            visit[nr][nc] = True
            q.append((nr, nc))
    # 상우
    if 0 <= r - 1 < R and 0 <= c + 1 < C:
        nr, nc = r - 1, c + 1
        if not exist_wall(r, c, 0) and not exist_wall(r, c + 1, 2) and not visit[nr][nc]:
            temperate[nr][nc] += t
            visit[nr][nc] = True
            q.append((nr, nc))


# 온풍기 아래쪽
def down(r, c, t, visit, q):
    # 하
    if 0 <= r + 1 < R:
        nr, nc = r + 1, c
        # 사이에 벽이 없고, 같은 온풍기 바람이 아직 안 왔으면
        if not exist_wall(r, c, 3) and not visit[nr][nc]:
            temperate[nr][nc] += t
            visit[nr][nc] = True
            q.append((nr, nc))
    # 하좌
    if 0 <= r + 1 < R and 0 <= c - 1 < C:
        nr, nc = r + 1, c - 1
        if not exist_wall(r, c, 1) and not exist_wall(r, c - 1, 3) and not visit[nr][nc]:
            temperate[nr][nc] += t
            visit[nr][nc] = True
            q.append((nr, nc))
    # 하우
    if 0 <= r + 1 < R and 0 <= c + 1 < C:
        nr, nc = r + 1, c + 1
        if not exist_wall(r, c, 0) and not exist_wall(r, c + 1, 3) and not visit[nr][nc]:
            temperate[nr][nc] += t
            visit[nr][nc] = True
            q.append((nr, nc))


# 온풍기 가동
def radiator_on():
    # 온풍기 개수만큼 가동
    for i in range(len(radiator)):
        rr, rc, rd = radiator[i]
        sr, sc = rr + dr[rd], rc + dc[rd]
        q = deque([(sr, sc)])
        visit = [[False] * C for _ in range(R)]
        temperate[sr][sc] += 5
        visit[sr][sc] = True
        for t in range(4, 0, -1):
            size = len(q)
            for _ in range(size):
                cr, cc = q.popleft()
                if rd == 0:
                    right(cr, cc, t, visit, q)
                elif rd == 1:
                    left(cr, cc, t, visit, q)
                elif rd == 2:
                    up(cr, cc, t, visit, q)
                elif rd == 3:
                    down(cr, cc, t, visit, q)


# 온도 조절
def controll_temperate():
    temp = copy.deepcopy(temperate)
    for i in range(R):
        for j in range(C):
            for d in range(4):
                nr, nc = i + dr[d], j + dc[d]
                # 범위 내이고, 인접 칸 온도가 더 낮고, 사이에 벽이 없다면 온도 조절
                if 0 <= nr < R and 0 <= nc < C and temperate[nr][nc] < temperate[i][j] and not exist_wall(i, j, d):
                    v = (temperate[i][j] - temperate[nr][nc]) // 4
                    temp[i][j] -= v
                    temp[nr][nc] += v

    # 조절된 온도 반영 & 영향준 온풍기 리셋
    for i in range(R):
        for j in range(C):
            temperate[i][j] = temp[i][j]


# 가장자리 온도 -1
def edge_minus():
    for i in range(C):
        temperate[0][i] = max(0, temperate[0][i] - 1)
        temperate[R - 1][i] = max(0, temperate[R - 1][i] - 1)
    for i in range(1, R - 1):
        temperate[i][0] = max(0, temperate[i][0] - 1)
        temperate[i][C - 1] = max(0, temperate[i][C - 1] - 1)


# 온도 조사
def check_temperate():
    for r, c in check:
        if temperate[r][c] < K:
            return False
    return True


# 입력 받기
R, C, K = map(int, input().split())

# 온도
temperate = [[0] * C for _ in range(R)]

# 온풍기와 조사할 위치 좌표
radiator = []
check = []
for i in range(R):
    line = [*map(int, input().split())]
    for j in range(C):
        if line[j] == 5:
            check.append((i, j))
        elif line[j] > 0:
            radiator.append([i, j, line[j] - 1])

# 벽 좌표
W = int(input())
wall = {}
for _ in range(W):
    r, c, mod = map(int, input().split())
    if (r - 1, c - 1) in wall:
        wall[(r - 1, c - 1)].append(mod)
    else:
        wall[(r - 1, c - 1)] = [mod]


# 시뮬레이션 시작
choco = 0
while not check_temperate():
    if choco > 100:
        break
    radiator_on()
    controll_temperate()
    edge_minus()
    choco += 1
print(choco)