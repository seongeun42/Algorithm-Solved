t = int(input())
num = [1, 2, 4]
for _ in range(t):
  n = int(input())
  for i in range(len(num), n):
    num.append(sum(num[i - 3:i]))
  print(num[n - 1])