n, k = map(int, input().split())
nums = [*map(int, input().split(','))]
for _ in range(k):
    new = []
    for i in range(1, len(nums)):
        new.append(nums[i] - nums[i - 1])
    nums = new
print(','.join(map(str, nums)))