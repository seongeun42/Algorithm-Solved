from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, jd, w, h):
  queue = deque([[x, y]])
  jd[y][x] = 0
  while queue:
    v = queue.popleft()
    if v[0] < w - 1 and jd[v[1]][v[0] + 1] == 1:
      queue.append([v[0] + 1, v[1]])
      jd[v[1]][v[0] + 1] = 0
    if v[0] > 0 and jd[v[1]][v[0] - 1] == 1:
      queue.append([v[0] - 1, v[1]])
      jd[v[1]][v[0] - 1] = 0
    if v[1] < h - 1 and jd[v[1] + 1][v[0]] == 1:
      queue.append([v[0], v[1] + 1])
      jd[v[1] + 1][v[0]] = 0
    if v[1] > 0 and jd[v[1] - 1][v[0]] == 1:
      queue.append([v[0], v[1] - 1])
      jd[v[1] - 1][v[0]] = 0

t = int(input())
for _ in range(t):
  m, n, k = map(int, input().split())
  jido = [[0] * m for _ in range(n)]
  loca = [list(map(int, input().split())) for _ in range(k)]
  for v in loca:
    jido[v[1]][v[0]] = 1
  cnt = 0

  for v in loca:
    if jido[v[1]][v[0]] == 1:
      bfs(v[0], v[1], jido, m, n)
      cnt += 1

  print(cnt)