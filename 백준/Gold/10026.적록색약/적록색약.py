from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10000)

N = int(input())
arr = [list(input().strip()) for _ in range(N)]

def dfs(x, y, color, changeTo):
  if arr[x][y] == color:
    arr[x][y] = changeTo
    if x - 1 >= 0 and arr[x - 1][y] == color:
      dfs(x - 1, y, color, changeTo)
    if x + 1 < N and arr[x + 1][y] == color:
      dfs(x + 1, y, color, changeTo)
    if y - 1 >= 0 and arr[x][y - 1] == color:
      dfs(x, y - 1, color, changeTo)
    if y + 1 < N and arr[x][y + 1] == color:
      dfs(x, y + 1, color, changeTo)

answer = [0, 0]
cnt = 0
for i in range(N):
  for j in range(N):
    if arr[i][j] == 'G':
      dfs(i, j, 'G', 0)
      cnt += 1
answer[0] += cnt

cnt = 0
for i in range(N):
  for j in range(N):
    if arr[i][j] == 'R':
      dfs(i, j, 'R', 0)
      cnt += 1
answer[0] += cnt

cnt = 0
for i in range(N):
  for j in range(N):
    if arr[i][j] == 0:
      dfs(i, j, 0, 1)
      cnt += 1
answer[1] += cnt

cnt = 0
for i in range(N):
  for j in range(N):
    if arr[i][j] == 'B':
      dfs(i, j, 'B', 1)
      cnt += 1
answer[1] += cnt
answer[0] += cnt

for a in answer:
  print(a, end=' ')