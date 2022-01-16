n = int(input())
t = sorted(list(map(int, input().split())))
res = 0
for i, v in enumerate(t):
  res += v * (n - i)
print(res)