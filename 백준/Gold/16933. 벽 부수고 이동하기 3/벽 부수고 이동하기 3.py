from collections import deque
import sys
input = sys.stdin.readline

def solve():
    N, M, K = map(int, input().split())
    arr = [input().rstrip() for _ in range(N)]
    visited = [[[1e9] * M for _ in range(N)] for _ in range(K + 1)]
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]
    # r, c, k, dist
    q = deque([(0, 0, 0, 1)])
    visited[0][0][0] = 1
    ans = 1e9
    while q:
        cr, cc, ck, dist = q.popleft()
        if cr == N - 1 and cc == M - 1:
            if dist < ans:
                ans = dist
            continue
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == '0' and dist + 1 < visited[ck][nr][nc]:
                    visited[ck][nr][nc] = dist + 1
                    q.append((nr, nc, ck, dist + 1))
                if arr[nr][nc] == '1' and ck < K and dist + 1 < visited[ck + 1][nr][nc]:
                    # 낮이면 벽 부수고 이동
                    if dist % 2:
                        visited[ck + 1][nr][nc] = dist + 1
                        q.append((nr, nc, ck + 1, dist + 1))
                    else:
                        # 밤이면 하루 대기
                        q.append((cr, cc, ck, dist + 1))
    print(ans if ans < 1e9 else -1)

solve()