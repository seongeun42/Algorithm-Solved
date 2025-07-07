import sys
input = sys.stdin.readline

def get_heart(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == '*':
                return [i + 1, j]

def solve():
    N = int(input())
    arr = [input().rstrip() for _ in range(N)]
    heart = get_heart(arr)
    larm, rarm = 0, 0
    for i in range(N):
        if arr[heart[0]][i] == '*':
            if i < heart[1]:
                larm += 1
            elif i > heart[1]:
                rarm += 1
    waist = [0, heart[1], 0]
    for i in range(heart[0] + 1, N):
        if arr[i][heart[1]] == '*':
            waist[2] += 1
        else:
            break
    waist[0] = heart[0] + waist[2]
    lleg = 0
    for i in range(1, N - waist[0]):
        if arr[waist[0] + i][waist[1] - 1] == '*':
            lleg += 1
        else:
            break
    rleg = 0
    for i in range(1, N - waist[0]):
        if arr[waist[0] + i][waist[1] + 1] == '*':
            rleg += 1
        else:
            break
    print(heart[0] + 1, heart[1] + 1)
    print(larm, rarm, waist[2], lleg, rleg)

solve()