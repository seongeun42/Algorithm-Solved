n, m = map(int, input().split())
c = list(map(int, input().split()))
for _ in range(m):
  c = sorted(c)
  c[0], c[1] = c[0] + c[1], c[0] + c[1]
print(sum(c))