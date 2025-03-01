C, R = map(int, input().split())
K = int(input())
if K > C * R:
    print(0)
else:
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0
    chk = [[False] * C for _ in range(R)]
    chk[0][0] = True
    cx, cy = 0, 0
    while K > 1:
        nx, ny = cx + direction[d][0], cy + direction[d][1]
        if 0 <= nx < C and 0 <= ny < R and not chk[ny][nx]:
            chk[ny][nx] = True
            cx, cy = nx, ny
            K -= 1
        else:
            d = (d + 1) % 4
    print(cx + 1, cy + 1)