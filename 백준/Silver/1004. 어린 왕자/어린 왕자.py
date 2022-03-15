T = int(input())
for _ in range(T):
  x1, y1, x2, y2 = map(int, input().split())
  n = int(input())
  p = [[*map(int, input().split())] for _ in range(n)]
  cnt = 0
  for a, b, r in p:
    s = (x1 - a) ** 2 + (y1 - b) ** 2
    e = (x2 - a) ** 2 + (y2 - b) ** 2
    if s < r ** 2 and e < r ** 2:
      continue
    elif s < r ** 2:
      cnt += 1
    elif e < r ** 2:
      cnt += 1
  print(cnt)