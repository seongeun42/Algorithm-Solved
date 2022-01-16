import sys
input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
room[r][c], cnt = -1, 1
rotate = 0
while True:
  if rotate == 4:
    b = d - 2 if d > 1 else d + 2
    if room[r + dy[b]][c + dx[b]] == 1:
      break
    else:
      r, c = r + dy[b], c + dx[b]
      rotate = 0
  else:
    d = d - 1 if d else 3
    rotate += 1
    if room[r + dy[d]][c + dx[d]] == -1 or room[r + dy[d]][c + dx[d]] == 1:
      continue
    elif room[r + dy[d]][c + dx[d]] == 0:
      r, c = r + dy[d], c + dx[d]
      room[r][c] = -1
      cnt += 1
      rotate = 0
print(cnt)