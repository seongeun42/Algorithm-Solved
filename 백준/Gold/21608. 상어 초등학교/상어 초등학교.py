def sit(kid, f):
    nullCnt = 0
    friendCnt = 0
    r, c = 0, 0
    for i in range(N):
        for j in range(N):
            if pan[i][j] == 0:
                nc, fc = 0, 0
                for k in range(4):
                    nx, ny = j + dx[k], i + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if pan[ny][nx] == 0:
                            nc += 1
                        elif pan[ny][nx] in f:
                            fc += 1
                if friendCnt < fc or (friendCnt == fc and nullCnt < nc) or pan[r][c] != 0:
                    r, c = i, j
                    nullCnt, friendCnt = nc, fc
    pan[r][c] = kid

N = int(input())
S = {}
for _ in range(N * N):
    s = [*map(int, input().split())]
    S[s[0]] = s[1:]
pan = [[0] * N for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
res = 0

for k, v in S.items():
    sit(k, v)

for i in range(N):
    for j in range(N):
        cnt = 0
        for k in range(4):
            nx, ny = j + dx[k], i + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if pan[ny][nx] in S[pan[i][j]]:
                    cnt += 1
        if cnt:
            res += 10 ** (cnt - 1)

print(res)