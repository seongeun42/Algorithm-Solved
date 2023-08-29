import sys, copy
input = sys.stdin.readline

ans = 0

def moveUp(arr, dep):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j][0] == 0:
                continue
            ny = i - 1
            while ny >= 0 and arr[ny][j][0] == 0:
                ny -= 1
            if ny >= 0 and arr[ny][j][0] == arr[i][j][0] and arr[ny][j][1] < dep:
                arr[ny][j] = [arr[ny][j][0] * 2, dep]
                arr[i][j] = [0, 0]
            elif i != ny + 1:
                arr[ny + 1][j], arr[i][j] = arr[i][j], [0, 0]

def moveDown(arr, dep):
    for i in range(len(arr) - 1, -1, -1):
        for j in range(len(arr)):
            if arr[i][j][0] == 0:
                continue
            ny = i + 1
            while ny < len(arr) and arr[ny][j][0] == 0:
                ny += 1
            if ny < len(arr) and arr[ny][j][0] == arr[i][j][0] and arr[ny][j][1] < dep:
                arr[ny][j] = [arr[ny][j][0] * 2, dep]
                arr[i][j] = [0, 0]
            elif i != ny - 1:
                arr[ny - 1][j], arr[i][j] = arr[i][j], [0, 0]

def moveLeft(arr, dep):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j][0] == 0:
                continue
            nx = j - 1
            while nx >= 0 and arr[i][nx][0] == 0:
                nx -= 1
            if nx >= 0 and arr[i][nx][0] == arr[i][j][0] and arr[i][nx][1] < dep:
                arr[i][nx] = [arr[i][nx][0] * 2, dep]
                arr[i][j] = [0, 0]
            elif j != nx + 1:
                arr[i][nx + 1], arr[i][j] = arr[i][j], [0, 0]

def moveRight(arr, dep):
    for i in range(len(arr)):
        for j in range(len(arr) - 1, -1, -1):
            if arr[i][j][0] == 0:
                continue
            nx = j + 1
            while nx < len(arr) and arr[i][nx][0] == 0:
                nx += 1
            if nx < len(arr) and arr[i][nx][0] == arr[i][j][0] and arr[i][nx][1] < dep:
                arr[i][nx] = [arr[i][nx][0] * 2, dep]
                arr[i][j] = [0, 0]
            elif j != nx - 1:
                arr[i][nx - 1], arr[i][j] = arr[i][j], [0, 0]

def move(pan, d, dep):
    tmp = copy.deepcopy(pan)
    if d == 0:
        moveUp(tmp, dep)
    elif d == 1:
        moveDown(tmp, dep)
    elif d == 2:
        moveLeft(tmp, dep)
    elif d == 3:
        moveRight(tmp, dep)
    return tmp


def backtrack(dep, pan):
    global ans
    if dep > 5:
        for i in range(len(pan)):
            for j in range(len(pan)):
                if pan[i][j][0] > ans:
                    ans = pan[i][j][0]
        return

    for i in range(4):
        after = move(pan, i, dep)
        backtrack(dep + 1, after)

def solve():
    global ans
    N = int(input())
    arr = [[] for _ in range(N)]
    for i in range(N):
        line = [*map(int, input().split())]
        for j in range(N):
            arr[i].append([line[j], 0])
    backtrack(1, arr)
    print(ans)

solve()