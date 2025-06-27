import sys, heapq
input = sys.stdin.readline

def find_enterprise(arr):
    for i, line in enumerate(arr):
        for j, c in enumerate(line):
            if c == 'E':
                return (i, j)

def is_edge(r, c, H, W):
    if r in {0, H - 1} or c in {0, W - 1}:
        return True
    return False

def dijkstra(arr, start, H, W, ships):
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    hq = [(0, start[0], start[1])]
    dp = [[1e9] * W for _ in range(H)]
    dp[start[0]][start[1]] = 0
    while hq:
        cw, cnr, cnc = heapq.heappop(hq)
        if is_edge(cnr, cnc, H, W):
            return cw
        if dp[cnr][cnc] < cw:
            continue
        for d in range(4):
            nnr, nnc = cnr + dr[d], cnc + dc[d]
            if 0 <= nnr < H and 0 <= nnc < W:
                nw = ships[arr[nnr][nnc]]
                if cw + nw < dp[nnr][nnc]:
                    dp[nnr][nnc] = cw + nw
                    heapq.heappush(hq, (cw + nw, nnr, nnc))

def solve():
    T = int(input())
    for _ in range(T):
        K, W, H = map(int, input().split())
        ships = {'E': 0}
        for _ in range(K):
            al, time = input().rstrip().split()
            ships[al] = int(time)
        arr = [input().rstrip() for _ in range(H)]
        print(dijkstra(arr, find_enterprise(arr), H, W, ships))

solve()