R, C = map(int, input().split())
bf = [input() for _ in range(R)]
af = [['.'] * C for _ in range(R)]
dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]
min_r, min_c = 10, 10
max_r, max_c = -1, -1
for i in range(R):
    for j in range(C):
        if bf[i][j] == 'X':
            cnt = 0
            for x, y in dir:
                ni, nj = i + y, j + x
                if 0 <= ni < R and 0 <= nj < C:
                    if bf[ni][nj] == '.':
                        cnt += 1
                else:
                    cnt += 1
            if cnt < 3:
                af[i][j] = 'X'
                min_r = min(i, min_r)
                min_c = min(j, min_c)
                max_r = max(i, max_r)
                max_c = max(j, max_c)
for i in range(min_r, max_r + 1):
    for j in range(min_c, max_c + 1):
        print(af[i][j], end='')
    print()