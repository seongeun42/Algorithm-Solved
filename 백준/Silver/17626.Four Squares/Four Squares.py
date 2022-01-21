def find(n):
  v = n ** 0.5
  if int(v) == v:
    return 1
  for i in range(int(v) + 1):
    k = n - i ** 2
    if int(k ** 0.5) == k ** 0.5:
      return 2
  for i in range(int(v) + 1):
    k = n - i ** 2
    for j in range(int(k ** 0.5) + 1):
      if int((k - j ** 2) ** 0.5) == (k - j ** 2) ** 0.5:
        return 3
  return 4

print(find(int(input())))