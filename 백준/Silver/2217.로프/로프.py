import sys
input = sys.stdin.readline
n = int(input())
lope = sorted([int(input()) for _ in range(n)], reverse=True)
w = 0
for i in range(n):
  w = max(w, lope[i] * (i + 1))
print(w)