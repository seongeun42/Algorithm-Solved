import sys
input = sys.stdin.readline

def solve():
    H, W = map(int, input().split())
    sand = [list(input().rstrip()) for _ in range(H)]
    dr = [0, 0, 1, -1, 1, -1, 1, -1]
    dc = [1, -1, 1, -1, -1, 1, 0, 0]
    # 초기 모래성 인접 빈공간 개수 기록
    cnt = {}
    # 초기에 부서질 모래성
    broken = []
    for i in range(H):
        for j in range(W):
            if sand[i][j] in ".9":
                continue
            if (i, j) not in cnt:
                cnt[(i, j)] = 0
            for d in range(8):
                nr, nc = i + dr[d], j + dc[d]
                if 0 <= nr < H and 0 <= nc < W and sand[nr][nc] == '.':
                    cnt[(i, j)] += 1
            if int(sand[i][j]) <= cnt[(i, j)]:
                broken.append((i, j))
    ans = 0
    while broken:
        ans += 1
        new_broken = []
        # 모래성 부수기
        for r, c in broken:
            sand[r][c] = '.'
            for d in range(8):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < H and 0 <= nc < W and sand[nr][nc] not in ".9":
                    cnt[(nr, nc)] += 1
                    # 다음에 부서질 모래성 추가
                    if cnt[(nr, nc)] == int(sand[nr][nc]):
                        new_broken.append((nr, nc))
        broken = new_broken
    print(ans)

solve()