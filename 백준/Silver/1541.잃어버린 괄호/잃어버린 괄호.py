nums = [sum(list(map(int, v.split('+')))) for v in list(input().split('-'))]
res = nums[0]
for i in range(1, len(nums)):
  res -= nums[i]
print(res)