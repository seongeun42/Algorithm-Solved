import sys, copy
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def fish_move(area, fish):
    newArea = copy.deepcopy(area)
    newFish = copy.deepcopy(fish)
    for i in range(1, 17):
        if newFish[i] == None:
            continue
        cx, cy = newFish[i]
        nx, ny = cx, cy
        cnt = 0
        while cnt < 8:
            nx, ny = cx + dx[newArea[cx][cy][1]], cy + dy[newArea[cx][cy][1]]
            if 0 > nx or nx >= 4 or 0 > ny or ny >= 4 or newArea[nx][ny] == 0:
                cnt += 1
                newArea[cx][cy][1] = (newArea[cx][cy][1] + 1) % 8
            else:
                nxt = newArea[nx][ny]
                if nxt == None:
                    newFish[i] = [nx, ny]
                else:
                    newFish[i], newFish[nxt[0]] = [nx, ny], [cx, cy]
                newArea[cx][cy], newArea[nx][ny] = nxt, newArea[cx][cy]
                break
    return newArea, newFish

def backtrack(area, fish, shark, dep):
    if dep >= 16:
        return sum(range(17))
    # 물고기 이동
    movedArea, movedFish = fish_move(area, fish)
    # 상어 이동
    d = shark[3]
    cx, cy = shark[:2]
    nx, ny = cx + dx[d], cy + dy[d]
    hap = shark[2]
    while 0 <= nx < 4 and 0 <= ny < 4:
        if movedArea[nx][ny] != None:
            fishNum, fishDirect = movedArea[nx][ny]
            movedArea[nx][ny] = 0
            movedArea[cx][cy] = None
            movedFish[fishNum] = None
            hap = max(hap, backtrack(movedArea, movedFish, [nx, ny, shark[2] + fishNum, fishDirect], dep + 1))
            movedArea[nx][ny] = [fishNum, fishDirect]
            movedArea[cx][cy] = 0
            movedFish[fishNum] = [nx, ny]
        nx, ny = nx + dx[d], ny + dy[d]
    return hap

def solve():
    area = [[] for _ in range(4)]
    fish = {}
    for i in range(4):
        l = [*map(int, input().split())]
        for j in range(4):
            area[i].append([l[j * 2], l[j * 2 + 1] - 1])
            fish[area[i][j][0]] = [i, j]
    shark = [0, 0, *area[0][0]]
    fish[area[0][0][0]] = None
    area[0][0] = 0
    print(backtrack(area, fish, shark, 0))

solve()