N = int(input())
nums = [*map(int, input().split())]
ans = 0
for i in range(N):
    if nums[i] != i + 1:
        ans += 1
print(ans)