def make_coordi(arr):
    res = []
    for i in range(1, len(arr) - 1, 2):
        res.append([arr[i] - 1, arr[i + 1] - 1])
    return res

n, m = map(int, input().split())
pan = [[0] * m for _ in range(n)]
qd = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
kd = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
Q = make_coordi([*map(int, input().split())])
K = make_coordi([*map(int, input().split())])
P = make_coordi([*map(int, input().split())])

for r, c in P:
    pan[r][c] = 3
for r, c in K:
    pan[r][c] = 2
for r, c in Q:
    pan[r][c] = 1

for r, c in Q:
    for dr, dc in qd:
        nr, nc = r + dr, c + dc
        while 1:
            if not (0 <= nr < n and 0 <= nc < m and pan[nr][nc] != 2 and pan[nr][nc] != 3):
                break
            pan[nr][nc] = 1
            nr += dr
            nc += dc

for r, c in K:
    for dr, dc in kd:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and not pan[nr][nc]:
            pan[nr][nc] = 2

res = 0
for i in range(n):
    res += pan[i].count(0)
print(res)