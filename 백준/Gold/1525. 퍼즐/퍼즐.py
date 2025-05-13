from collections import deque
import sys
input = sys.stdin.readline

def solve():
    arr = []
    empty = None
    for i in range(3):
        a = [*map(int, input().split())]
        for j in range(3):
            arr.append(a[j])
            if a[j] == 0:
                empty = len(arr) - 1
    ordered = tuple(sorted(arr)[1:] + [0])
    nxt = {0: (1, 3), 1: (0, 2, 4), 2: (1, 5),
           3: (0, 4, 6), 4: (1, 3, 5, 7), 5: (2, 4, 8),
           6: (3, 7), 7: (4, 6, 8), 8: (5, 7)}
    visited = {tuple(arr)}
    q = deque([(0, empty, tuple(arr))])
    while q:
        cnt, cur_lo, cur_arr = q.popleft()
        if cur_arr == ordered:
            print(cnt)
            return
        for nxt_lo in nxt[cur_lo]:
            nxt_arr = list(cur_arr)
            nxt_arr[cur_lo], nxt_arr[nxt_lo] = nxt_arr[nxt_lo], nxt_arr[cur_lo]
            nxt_arr = tuple(nxt_arr)
            if nxt_arr not in visited:
                visited.add(nxt_arr)
                q.append((cnt + 1, nxt_lo, nxt_arr))
    print(-1)
    return

solve()