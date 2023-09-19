import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def find_root(r, c, R):
    if R[r][c] != [r, c]:
        R[r][c] = find_root(R[r][c][0], R[r][c][1], R)
    return R[r][c]

def solve():
    N, M, Q = map(int, input().split())
    H = [[*map(int, input().split())] for _ in range(N)]
    # 물 있는지 여부와 내린 날
    water = [[[0, 0] for _ in range(M)] for _ in range(N)]
    # 루트 기록 : 루트는 각 집합 내 가장 오래되고 최저인 높이 좌표
    R = [[[j, i] for i in range(M)] for j in range(N)]
    for q in range(Q):
        a, b, c = map(int, input().split())
        a, b = a - 1, b - 1
        H[a][b] -= c
        water[a][b][0] = 1
        water[a][b][1] = q
        for d in range(4):
            ny = a + dy[d]
            nx = b + dx[d]
            if 0 <= ny < N and 0 <= nx < M and water[ny][nx][0] == 1:
                r1 = find_root(a, b, R)
                r2 = find_root(ny, nx, R)
                if r1 != r2: # 다른 집합일 때
                    # 높이가 더 낮은 곳으로 유니온, 같다면 더 오래된 곳
                    if H[r1[0]][r1[1]] < H[r2[0]][r2[1]]:
                        R[r2[0]][r2[1]] = r1
                    elif H[r1[0]][r1[1]] > H[r2[0]][r2[1]]:
                        R[r1[0]][r1[1]] = r2
                    elif water[r1[0]][r1[1]][1] < water[r2[0]][r2[1]][1]:
                        R[r2[0]][r2[1]] = r1
                    else:
                        R[r1[0]][r1[1]] = r2
                else:
                    # 같은 집합일 때, 새로 비 온 칸의 높이가 더 낮으면 루트 갱신
                    if H[a][b] < H[r1[0]][r1[1]]:
                        R[a][b] = [a, b]
                        R[r1[0]][r1[1]] = [a, b]
        root = find_root(a, b, R)
        print(R[root[0]][root[1]][0] + 1, R[root[0]][root[1]][1] + 1)

solve()