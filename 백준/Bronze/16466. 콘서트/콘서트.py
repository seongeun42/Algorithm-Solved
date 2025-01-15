n = int(input())
nums = sorted([*map(int, input().split())])
for i in range(n):
    if (i + 1) != nums[i]:
        print(i + 1)
        break
else:
    print(n + 1)