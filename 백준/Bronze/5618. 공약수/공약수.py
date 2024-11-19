import math

n = int(input())
nums = [*map(int, input().split())]
gcd = math.gcd(nums[0], nums[1])
if n == 3:
    gcd = math.gcd(gcd, nums[2])
ans = set()
for i in range(1, int(gcd ** 0.5)+1):
    if gcd % i == 0:
        ans.add(i)
        ans.add(gcd // i)
for i in sorted(ans):
    print(i)