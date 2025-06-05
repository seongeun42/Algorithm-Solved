import sys, heapq
input = sys.stdin.readline

def find_count(arr, start, N, M):
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    hq = [(0, start[0], start[1])]
    visited = [[N * N] * N for _ in range(N)]
    visited[start[0]][start[1]] = 0
    connected = {start}
    cnt = 0
    while hq:
        c_dist, cr, cc = heapq.heappop(hq)
        if arr[cr][cc] == 'K' and (cr, cc) not in connected:
            heapq.heappush(hq, (0, cr, cc))
            connected.add((cr, cc))
            cnt += c_dist
        if len(connected) == M + 1:
            return cnt
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != '1':
                if visited[nr][nc] > c_dist + 1:
                    visited[nr][nc] = c_dist + 1
                    heapq.heappush(hq, (c_dist + 1, nr, nc))
                        
    return -1

def solve():
    N, M = map(int, input().split())
    arr = [input().rstrip() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'S':
                return find_count(arr, (i, j), N, M)

print(solve())