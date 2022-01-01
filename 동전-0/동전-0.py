import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin = coin[::-1]
cnt = 0
for v in coin:
  if not k:
    break
  if v > k:
    continue
  cnt += k // v
  k = k % v
print(cnt)