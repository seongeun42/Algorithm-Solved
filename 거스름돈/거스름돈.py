n = 1000 - int(input())
cnt = 0
coin = [500, 100, 50, 10, 5, 1]
for v in coin:
  if not n: break
  cnt += n // v
  n %= v
print(cnt)