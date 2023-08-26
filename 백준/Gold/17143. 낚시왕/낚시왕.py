import sys
input = sys.stdin.readline

def solve():
    R, C, M = map(int, input().split())
    sea = [[[] for _ in range(C)] for _ in range(R)]
    shark = []
    candi = [R] * C
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        shark.append((r - 1, c - 1))
        sea[r - 1][c - 1] = (s, d, z)
        if candi[c - 1] > r - 1:
            candi[c - 1] = r - 1
    
    cnt = 0
    ans = 0
    while (cnt < C):
        if candi[cnt] != R:
            ans += sea[candi[cnt]][cnt][2]
            sea[candi[cnt]][cnt] = []
        sharkList = []
        newCandi = [R] * C
        while shark:
            r, c = shark.pop()
            if len(sea[r][c]) == 0:
                continue
            s, d, z = sea[r][c]
            sea[r][c] = []
            sharkList.append((r, c, s, d, z))
        for r, c, s, d, z in sharkList:
            nr, nc = r, c
            if d == 1:
                s %= (R - 1) * 2
                nr = r - s
                if nr < 0:
                    if abs(nr) >= R - 1:
                        nr += 2 * (R - 1)
                    else:
                        d = 2
                        nr = abs(nr)
            elif d == 2:
                s %= (R - 1) * 2
                nr = r + s
                if nr >= R:
                    if nr >= 2 * (R - 1):
                        nr -= 2 * (R - 1)
                    else:
                        d = 1
                        nr = 2 * (R - 1) - nr
            elif d == 3:
                s %= (C - 1) * 2
                nc = c + s
                if nc >= C:
                    if nc >= 2 * (C - 1):
                        nc -= 2 * (C - 1)
                    else:
                        d = 4
                        nc = 2 * (C - 1) - nc
            elif d == 4:
                s %= (C - 1) * 2
                nc = c - s
                if nc < 0:
                    if abs(nc) >= C - 1:
                        nc += 2 * (C - 1)
                    else:
                        d = 3
                        nc = abs(nc)
            # print("ss : ", nr, nc, s, d, z)
            if newCandi[nc] > nr:
                newCandi[nc] = nr
            if len(sea[nr][nc]) == 0 or sea[nr][nc][2] < z:
                sea[nr][nc] = (s, d, z)
            shark.append((nr, nc))
        candi = newCandi
        cnt += 1
    print(ans)

solve()