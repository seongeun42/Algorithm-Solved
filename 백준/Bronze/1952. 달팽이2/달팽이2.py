M, N = map(int, input().split())
arr = [[0] * N for _ in range(M)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = 0
dir, visit = 0, 1
cx, cy = 0, 0
while visit < M * N:
    arr[cy][cx] = 1
    while 0 <= cx + dx[dir] < N and 0 <= cy + dy[dir] < M and arr[cy + dy[dir]][cx + dx[dir]] == 0:
        cx += dx[dir]
        cy += dy[dir]
        arr[cy][cx] = 1
        visit += 1
    dir = (dir + 1) % 4
    ans += 1
print(ans - 1)