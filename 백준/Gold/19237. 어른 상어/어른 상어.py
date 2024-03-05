import sys
input = sys.stdin.readline

N, M, k = map(int, input().split())
sharkLoca = {}
arr = []
for i in range(N):
    arr.append([])
    l = [*map(int, input().split())]
    for j in range(N):
        arr[i].append(l[j])
        if l[j] != 0:
            sharkLoca[l[j]] = (i, j)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 방향 기록
sharkDir = [-1] + [*map(int, input().split())]
sharkPriory = {i + 1: {} for i in range(M)}
for i in range(1, M + 1):
    for j in range(1, 5):
        sharkPriory[i][j] = tuple(map(int, input().split()))

# 냄새
smell = {}
for i in range(1, M + 1):
    smell[sharkLoca[i]] = [i, k]
    
cnt = M
time = 0
while cnt > 1:
    if time >= 1000:
        time = -1
        break
    time += 1
    for i in range(1, M + 1):
        if sharkLoca[i] == -1:
            continue
        priory = sharkPriory[i][sharkDir[i]]
        cy, cx = sharkLoca[i]
        if arr[cy][cx] == i:
            arr[cy][cx] = 0
        moved = False
        for d in priory:
            ny, nx = cy + dy[d - 1], cx + dx[d - 1]
            if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in smell:
                if arr[ny][nx] == 0 or arr[ny][nx] > i:
                    arr[ny][nx] = i
                    sharkLoca[i] = (ny, nx)
                    sharkDir[i] = d
                else:
                    sharkLoca[i] = -1
                    cnt -= 1
                moved = True
                break
        if not moved:
            for d in priory:
                ny, nx = cy + dy[d - 1], cx + dx[d - 1]
                if 0 <= ny < N and 0 <= nx < N and smell[(ny, nx)][0] == i:
                    arr[ny][nx] = i
                    sharkLoca[i] = (ny, nx)
                    sharkDir[i] = d
                    break
    # 냄새
    del_list = []
    for key, value in smell.items():
        if value[1] == 1:
            del_list.append(key)
        else:
            smell[key][1] -= 1
    for v in del_list:
        del smell[v]
    for i in range(1, M + 1):
        smell[sharkLoca[i]] = [i, k]

print(time)