import sys
input = sys.stdin.readline
sl = list(input().strip())
sr = []
n = int(input())
for _ in range(n):
  op = input().split()
  if op[0] == 'P':
    sl.append(op[1])
  if op[0] == 'L' and sl:
    sr.append(sl.pop())
  if op[0] == 'D' and sr:
    sl.append(sr.pop())
  if op[0] == 'B' and sl:
    sl.pop()
print(''.join(sl + sr[::-1]))