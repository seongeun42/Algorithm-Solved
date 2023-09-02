import sys
K, N = map(int, sys.stdin.readline().split())
k = [int(sys.stdin.readline()) for _ in range(K)]
s, res = 0, sum(k) // N
while s <= res:
  mid = (s + res) // 2 if (s + res) // 2 else 1
  n = 0
  for v in k:
    n += v // mid
  if n >= N: s = mid + 1
  else: res = mid - 1
print(res)