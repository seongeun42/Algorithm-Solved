n = int(input())
t = list(map(int, input().split()))
y, m = 0, 0
for v in t:
  y += 10 * (v // 30 + 1)
  m += 15 * (v // 60 + 1)
if y < m:
  print('Y', y)
elif y > m:
  print('M', m)
else:
  print('Y', 'M', y)