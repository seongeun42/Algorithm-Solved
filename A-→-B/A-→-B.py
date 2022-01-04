a, b = map(int, input().split())
cnt = 0
while a != b and b:
  if not b % 2:
    b //= 2
  elif b % 10 == 1:
    b -= 1
    b //= 10
  else: break
  cnt += 1
print(cnt + 1 if a == b else -1)