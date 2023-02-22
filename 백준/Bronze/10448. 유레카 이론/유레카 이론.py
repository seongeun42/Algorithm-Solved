tn = [n * (n + 1) // 2 for n in range(1, 45)]
nums = [0] * 1001
for i in tn:
    for j in tn:
        for k in tn:
            if i + j + k <= 1000:
                nums[i + j + k] = 1
t = int(input())
for _ in range(t):
    print(nums[int(input())])