from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def is_connected(idxs):
    visited = set()
    def dfs(cur):
        cnt = 1
        visited.add(cur)
        for d in range(4):
            nr, nc = cur[0] + dr[d], cur[1] + dc[d]
            if (nr, nc) in idxs and (nr, nc) not in visited:
                cnt += dfs((nr, nc))
        return cnt
    return dfs(idxs[0]) == len(idxs)

def bfs(init_bits):
    q = deque([(init_bits, 0)])
    visited = {init_bits}
    while q:
        cur, cnt = q.popleft()
        idxs = [divmod(i, 5) for i in range(25) if cur & (1 << i)]
        if is_connected(idxs):
            return cnt
        for cr, cc in set(idxs):
            for d in range(4):
                nr, nc = cr + dr[d], cc + dc[d]
                if 0 <= nr < 5 and 0 <= nc < 5 and (nr, nc) not in idxs:
                    nxt = cur & ~(1 << (cr * 5 + cc))
                    nxt |= (1 << (nr * 5 + nc))
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, cnt + 1))

def solve():
    arr = [input().rstrip() for _ in range(5)]
    bits = 0
    for i in range(5):
        for j in range(5):
            if arr[i][j] == '*':
                bits |= (1 << (i * 5 + j))
    print(bfs(bits))

solve()