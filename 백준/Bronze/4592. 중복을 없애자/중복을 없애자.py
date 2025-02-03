while 1:
    nums = [*map(int, input().split())]
    if nums[0] == 0:
        break
    for i in range(1, nums[0] + 1):
        if i == 1 or nums[i] != nums[i - 1]:
            print(nums[i], end=" ")
    print("$")