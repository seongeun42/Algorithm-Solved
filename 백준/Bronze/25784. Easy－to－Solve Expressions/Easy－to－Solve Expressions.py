nums = sorted([*map(int, input().split())])
if nums[0] + nums[1] == nums[2]:
    print(1)
elif nums[0] * nums[1] == nums[2]:
    print(2)
else:
    print(3)