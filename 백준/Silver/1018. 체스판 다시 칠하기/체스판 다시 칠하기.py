n, m = map(int, input().split())
p = []
re = []
for i in range(n):
  p.append(input())
for i in range(n - 7):
  for j in range(m - 7):
    s_w = 0
    s_b = 0
    for a in range(i, i + 8):
      for b in range(j, j + 8):
        if (a + b) % 2 == 0:
          if p[a][b] != 'W': s_w += 1
          if p[a][b] != 'B': s_b += 1
        else:
          if p[a][b] != 'W': s_b += 1
          if p[a][b] != 'B': s_w += 1
    re.append(min(s_w, s_b))
print(min(re))