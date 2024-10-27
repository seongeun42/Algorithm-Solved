import sys
input = sys.stdin.readline

def min_locate(cr, cc, board):
    dy = [0, 0, 1, 1, 1, -1, -1, -1]
    dx = [1, -1, 0, 1, -1, 0, 1, -1]
    r, c = [cr, cc]
    for d in range(8):
        nr, nc = cr + dy[d], cc + dx[d]
        if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
            if board[nr][nc] < board[r][c]:
                r, c = nr, nc
    return r, c

def find_root(n, R):
    if R[n] < 0:
        return n
    R[n] = find_root(R[n], R)
    return R[n]

def solve():
    R, C = map(int, input().split())
    board = [[*map(int, input().split())] for _ in range(R)]
    root = [-1] * (R * C)
    for i in range(R):
        for j in range(C):
            mi, mj = min_locate(i, j, board)
            u = i * C + j
            v = mi * C + mj
            ur = find_root(u, root)
            vr = find_root(v, root)
            # 체스판에 적힌 정수가 더 작은 쪽으로 union
            if board[i][j] < board[mi][mj]:
                root[ur] += root[vr]
                root[vr] = ur
            elif board[i][j] > board[mi][mj]:
                root[vr] += root[ur]
                root[ur] = vr
    ans = ""
    for i in range(R):
        for j in range(C):
            if root[C * i + j] > 0:
                ans += "0 "
            else:
                ans += f"{-1 * root[C * i + j]} "
        if i != R - 1:
            ans += "\n"
    print(ans)

solve()