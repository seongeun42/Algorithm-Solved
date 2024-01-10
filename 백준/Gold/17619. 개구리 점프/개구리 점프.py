import sys
input = sys.stdin.readline

def find_root(n):
    if R[n] != n:
        R[n] = find_root(R[n])
    return R[n]

N, Q = map(int, input().split())
tree = []
for i in range(N):
    x1, x2, y = map(int, input().split())
    tree.append((x1, x2, y, i))
tree.sort()
R = [i for i in range(N)]
cur_x1, cur_x2, cur_y, cur_idx = tree[0]
for i in range(1, N):
    nxt_x1, nxt_x2, nxt_y, nxt_idx = tree[i]
    if cur_x1 <= nxt_x1 <= cur_x2:
        cr = find_root(cur_idx)
        nr = find_root(nxt_idx)
        if cr != nr:
            R[max(cr, nr)] = min(cr, nr)
        if nxt_x2 >= cur_x2:
            cur_x1, cur_x2, cur_y, cur_idx = nxt_x1, nxt_x2, nxt_y, nxt_idx
    else:
        cur_x1, cur_x2, cur_y, cur_idx = nxt_x1, nxt_x2, nxt_y, nxt_idx

for _ in range(Q):
    a, b = map(int, input().split())
    print(1 if find_root(a - 1) == find_root(b - 1) else 0)