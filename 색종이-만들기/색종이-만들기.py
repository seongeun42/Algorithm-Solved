def cutPaper(x, y, P, wb, n):
  isSame = True
  for i in range(y, y + n):
    for j in range(x, x + n):
      if P[y][x] != P[i][j]:
        isSame = False
        break
    if not isSame: break

  if isSame:
    if P[y][x]: wb[1] += 1
    else: wb[0] += 1
  else:
    v = n // 2
    cutPaper(x, y, P, wb, n // 2)
    cutPaper(x + v, y, P, wb, n // 2)
    cutPaper(x, y + v, P, wb, n // 2)
    cutPaper(x + v, y + v, P, wb, n // 2)

n = int(input())
P = [list(map(int, input().split())) for _ in range(n)]
wb = [0, 0]
cutPaper(0, 0, P, wb, n)
print(*wb, sep='\n')