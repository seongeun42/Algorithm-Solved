def convert(x, y, arr):
  for i in range(y, y + 3):
    for j in range(x, x + 3):
      arr[i][j] = not arr[i][j]

n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
b = [list(map(int, input())) for _ in range(n)]

cnt = 0
for i in range(n - 2):
  for j in range(m - 2):
    if a[i][j] != b[i][j]:
      convert(j, i, a)
      cnt += 1

no = False
for i in range(n):
  for j in range(m):
    if a[i][j] != b[i][j]:
      no = True
      break
  if no: break

print(-1 if no else cnt)