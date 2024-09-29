from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

def solve():
    arr = [input().rstrip() for _ in range(5)]
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
    ans = 0
    for pick in combinations(range(25), 7):
        chk = [[False] * 5 for _ in range(5)]
        scnt = 0
        for v in pick:
            chk[v // 5][v % 5] = True
            if arr[v // 5][v % 5] == 'S':
                scnt += 1
        if scnt >= 4:
            sr, sc = pick[0] // 5, pick[0] % 5
            q = deque([(sr, sc)])
            chk[sr][sc] = False
            max_len = 0
            while q:
                cr, cc = q.popleft()
                max_len += 1
                for d in range(4):
                    nr, nc = cr + dr[d], cc + dc[d]
                    if 0 <= nr < 5 and 0 <= nc < 5 and chk[nr][nc] == True:
                        chk[nr][nc] = False
                        q.append((nr, nc))
            if max_len == 7:
                ans += 1
    print(ans)

solve()