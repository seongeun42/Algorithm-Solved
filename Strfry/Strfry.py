import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
  s1, s2 = input().split()
  print("Possible" if sorted(s1) == sorted(s2) else "Impossible")
