import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
  s1, s2 = input().split()
  s1 = sorted(list(s1))
  s2 = sorted(list(s2))
  flag = True
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      flag = False
      break
  print("Possible" if flag else "Impossible")