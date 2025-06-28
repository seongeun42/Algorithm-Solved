import sys
input = sys.stdin.readline

def counter(arr, i, j):
    car = 0
    for n in range(2):
        for m in range(2):
            if arr[i + n][j + m] == '#':
                return -1
            if arr[i + n][j + m] == 'X':
                car += 1
    return car

R, C = map(int, input().split())
arr = [input().rstrip() for _ in range(R)]
cnt = [0] * 5
for i in range(R - 1):
    for j in range(C - 1):
        car = counter(arr, i, j)
        if car > -1:
            cnt[car] += 1
print(*cnt, sep='\n')