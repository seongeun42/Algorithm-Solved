odd = []
min = float('inf')
for _ in range(7):
  v = int(input())
  if v % 2:
    odd.append(v)
    if min > v:
      min = v
if len(odd):
  print(sum(odd), min, sep='\n')
else:
  print(-1)