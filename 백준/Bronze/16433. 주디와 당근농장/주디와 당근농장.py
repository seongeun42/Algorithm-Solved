N, R, C = map(int, input().split())
arr = [['.'] * N for _ in range(N)]
for i in range(0, N, 2):
    for j in range(0, N, 2):
        if R % 2 == C % 2:
            arr[i][j] = 'v'
            if i + 1 < N and j + 1 < N:
                arr[i + 1][j + 1] = 'v'
        else:
            if j + 1 < N:
                arr[i][j + 1] = 'v'
            if i + 1 < N:
                arr[i + 1][j] = 'v'
for v in arr:
    print(''.join(v))