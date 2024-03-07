import sys
input = sys.stdin.readline

# 상, 좌, 하, 우
sdy = [0, -1, 0, 1]
sdx = [-1, 0, 1, 0]

def fish_move(fishes, shark, smell):
    # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
    fdy = [-1, -1, 0, 1, 1, 1, 0, -1]
    fdx = [0, -1, -1, -1, 0, 1, 1, 1]
    new_fishes = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for fish in fishes[i][j]:
                moved = False
                for d in range(8):
                    d_idx = (fish - d) % 8
                    nx, ny = i + fdx[d_idx], j + fdy[d_idx]
                    if 0 <= nx < 4 and 0 <= ny < 4 and [nx, ny] != shark:
                        if (nx, ny) not in smell or smell[(nx, ny)] < 0:
                            new_fishes[nx][ny].append(d_idx)
                            moved = True
                            break
                if not moved:
                    new_fishes[i][j].append(fish)
    return new_fishes


def shark_path(fishes, sx, sy):
    max_cnt = -1
    path = [-1, -1, -1]
    for i in range(4):
        tmp_cnt = 0
        passed = set()
        nx, ny = sx + sdx[i], sy + sdy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            tmp_cnt = len(fishes[nx][ny])
            passed.add((nx, ny))
            for j in range(4):
                nnx, nny = nx + sdx[j], ny + sdy[j]
                if 0 <= nnx < 4 and 0 <= nny < 4:
                    tmp_cnt2 = tmp_cnt
                    if (nnx, nny) not in passed:
                        tmp_cnt2 += len(fishes[nnx][nny])
                        passed.add((nnx, nny))
                    for k in range(4):
                        nnnx, nnny = nnx + sdx[k], nny + sdy[k]
                        if 0 <= nnnx < 4 and 0 <= nnny < 4:
                            tmp_cnt3 = tmp_cnt2
                            if (nnnx, nnny) not in passed:
                                tmp_cnt3 += len(fishes[nnnx][nnny])
                            if max_cnt < tmp_cnt3:
                                max_cnt = tmp_cnt3
                                path[0], path[1], path[2] = i, j, k
    return path


def solve():
    M, S = map(int, input().split())
    fishes = [[[] for _ in range(4)] for _ in range(4)]
    for _ in range(M):
        fx, fy, d = map(int, input().split())
        fishes[fx - 1][fy - 1].append(d - 1)
    shark = [*map(int, input().split())]
    shark[0] -= 1
    shark[1] -= 1
    smell = {}

    for _ in range(S):
        # 2. 물고기 이동
        new_fishes = fish_move(fishes, shark, smell)
        
        # 3. 상어 이동
        path = shark_path(new_fishes, *shark)
        if path != [-1, -1, -1]:
            for d in path:
                shark[0] += sdx[d]
                shark[1] += sdy[d]
                if len(new_fishes[shark[0]][shark[1]]) > 0:
                    new_fishes[shark[0]][shark[1]] = []
                    smell[(shark[0], shark[1])] = 2

        # 4. 냄새 없어짐
        for key in smell.keys():
            smell[key] -= 1

        # 5. 복제 완료
        for i in range(4):
            for j in range(4):
                new_fishes[i][j] += fishes[i][j]
        fishes = new_fishes
    
    ans = 0
    for i in range(4):
        for j in range(4):
            ans += len(fishes[i][j])
    print(ans)

solve()