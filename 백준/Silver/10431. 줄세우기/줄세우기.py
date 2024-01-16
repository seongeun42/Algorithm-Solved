P = int(input())
for t in range(P):
    nums = [*map(int, input().split())][1:]
    ans = 0
    for i in range(1, 20):
        for j in range(0, i):
            if nums[j] > nums[i]:
                ans += 1
    print(t + 1, ans)