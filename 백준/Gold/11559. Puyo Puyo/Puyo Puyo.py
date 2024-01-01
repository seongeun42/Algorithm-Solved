from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, c):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([(x, y)])
    visit = {(x, y)}
    # 연결된 뿌요 세기
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < 6 and 0 <= ny < 12 and field[ny][nx] == c and (nx, ny) not in visit:
                visit.add((nx, ny))
                q.append((nx, ny))
    # 연결된 뿌요가 4개 이상이면 터트리기
    if len(visit) >= 4:
        for cx, cy in visit:
            field[cy][cx] = '.'
        return True
    return False

field = [list(input().rstrip()) for _ in range(12)]
cnt = 0
while True:
    explosion = False
    existPuyo = -1
    for i in range(11, -1, -1):
        for j in range(6):
            # 빈칸 아니고 뿌요면 확인
            if field[i][j] != '.':
                existPuyo = i
                if bfs(j, i, field[i][j]):
                    explosion = True
        # 뿌요가 없으면 break
        if existPuyo == -1:
            break
    # 터지지 않았으면 break
    if not explosion:
        break
    # 터졌으면 횟수 증가시키고, 남은 뿌요 아래로 내리기
    cnt += 1
    for i in range(6):
        for j in range(11, existPuyo - 1, -1):
            if field[j][i] == '.':
                puyo = j
                while puyo >= 0 and field[puyo][i] == '.':
                    puyo -= 1
                if puyo >= 0:
                    field[j][i] = field[puyo][i]
                    field[puyo][i] = '.'
print(cnt)