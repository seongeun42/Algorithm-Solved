nums = [0, 0] + [0, 1] * 502500
nums[2] = 1
for i in range(3, 10001):
    if nums[i]:
        for j in range(i + i, 1005001, i):
            nums[j] = 0

n = int(input())
while 1:
    s = str(n)
    if nums[n] and s == s[::-1]:
        print(n)
        break
    n += 1