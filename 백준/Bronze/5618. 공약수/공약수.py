import math

n = int(input())
nums = [*map(int, input().split())]
gcd = math.gcd(nums[0], nums[1])
if n == 3:
    gcd = math.gcd(gcd, nums[2])
for i in range(1, gcd // 2 + 1):
    if gcd % i == 0:
        print(i)
print(gcd)