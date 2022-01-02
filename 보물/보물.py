n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)
res = a[0] * b[0]
for i in range(1, n):
  res += a[i] * b[i]
print(res)