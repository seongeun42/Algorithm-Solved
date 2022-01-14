import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  k = list(input().strip())
  sl, sr = [], []
  for v in k:
    if v == '<' and sl:
      sr.append(sl.pop())
    if v == '>' and sr:
      sl.append(sr.pop())
    if v == '-' and sl:
      sl.pop()
    if v != '<' and v != '>' and v != '-':
      sl.append(v)
  print(''.join(sl+sr[::-1]))