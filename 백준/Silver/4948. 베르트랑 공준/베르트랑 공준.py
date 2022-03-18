nums = [0, 0] + [1] * 246911
for i in range(2, 498):
    if nums[i]:
        for j in range(i + i, 246913, i):
            nums[j] = 0
while 1:
    n = int(input())
    if not n:
        break
    print(sum(nums[n+1:2*n+1]))