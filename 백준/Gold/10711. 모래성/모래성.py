from collections import deque
import sys
input = sys.stdin.readline

def bfs(sand, H, W):
    dr = [0, 0, 1, -1, 1, -1, 1, -1]
    dc = [1, -1, 1, -1, -1, 1, 0, 0]
    q = deque([])
    for i in range(H):
        for j in range(W):
            if sand[i][j] == '.':
                q.append((i, j, 0))
    cnts = [[0] * W for _ in range(H)]
    ans = 0
    while q:
        cr, cc, wave_cnt = q.popleft()
        if ans < wave_cnt:
            ans = wave_cnt
        for d in range(8):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < H and 0 <= nc < W and sand[nr][nc] not in ".9":
                cnts[nr][nc] += 1
                if int(sand[nr][nc]) == cnts[nr][nc]:
                    sand[nr][nc] = '.'
                    q.append((nr, nc, wave_cnt + 1))
    return ans

def solve():
    H, W = map(int, input().split())
    sand = [list(input().rstrip()) for _ in range(H)]
    print(bfs(sand, H, W))

solve()