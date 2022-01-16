import sys
input = sys.stdin.readline
n = int(input())
t = [list(map(int, input().split())) for _ in range(n)]
t = sorted(t, key=lambda x: (x[1], x[0]))
c, cnt = [0, 0], 0
for v in t:
  if v[0] < c[1]:
    continue
  cnt += 1
  c = v
print(cnt)