n, k = map(int, input().split())
nums = [True] * (n + 1)
for i in range(2, n + 1):
  if nums[i]:
    for j in range(i, n + 1, i):
      if nums[j]:
        nums[j] = False
        k -= 1
        if not k:
          print(j)
          break
  if not k:
    break