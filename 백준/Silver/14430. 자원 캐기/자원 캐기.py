import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            arr[i][j] += arr[i][j - 1]
        elif j == 0:
            arr[i][j] += arr[i - 1][j]
        else:
            arr[i][j] += max(arr[i - 1][j], arr[i][j - 1])
print(arr[N - 1][M - 1])