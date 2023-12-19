import sys
input = sys.stdin.readline
M = int(input())
s = [False] * 20
for _ in range(M):
  cmd = input().split()
  if len(cmd) == 1:
    s = [True] * 20 if cmd[0][0] == 'a' else [False] * 20
  else:
    n = int(cmd[1]) - 1
    if cmd[0][0] == 'a':
      s[n] = True
    elif cmd[0][0] == 'r':
      s[n] = False
    elif cmd[0][0] == 'c':
      sys.stdout.write('1\n' if s[n] else '0\n')
    else:
      s[n] = not s[n]