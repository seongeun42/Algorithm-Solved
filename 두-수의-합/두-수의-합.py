n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())
l, r = 0, n - 1
cnt = 0

while l < r:
  v = nums[l] + nums[r]
  if v == x:
    cnt += 1
  if v > x:
    r -= 1
  if v <= x:
    l += 1

print(cnt)