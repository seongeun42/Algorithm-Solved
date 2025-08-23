def sgs(nums):
    min_num = 9999
    for i in range(4):
        v = int(''.join(nums[i:4] + nums[:i]))
        if v < min_num:
            min_num = v
    return min_num

nums = list(input().split())
min_num = sgs(nums)
ans = 1
for i in range(1111, min_num):
    if '0' not in str(i):
        if i == sgs(list(str(i))):
            ans += 1
print(ans)