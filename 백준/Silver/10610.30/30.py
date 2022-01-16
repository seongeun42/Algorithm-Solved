n = sorted(list(map(int, list(input()))), reverse=True)
if not n[-1] and not (sum(n) % 3):
  print("".join(list(map(str, n))))
else:
  print(-1)