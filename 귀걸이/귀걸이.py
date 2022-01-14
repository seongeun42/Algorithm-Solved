from collections import defaultdict
import sys
input = sys.stdin.readline
cnt = 0
while 1:
  cnt += 1
  n = int(input())
  if not n: break
  names = [input().strip() for _ in range(n)]
  cases = [list(input().split()) for _ in range(2 * n - 1)]
  chk = defaultdict(int)
  for v in cases:
    chk[v[0]] += 1
  for k, v in chk.items():
    if v != 2: print(cnt, names[int(k) - 1])