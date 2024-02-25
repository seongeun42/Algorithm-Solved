N, K = map(int, input().split())
A = [*map(int, input().split())]
hap = [A[0]]
ans = 0 if A[0] != K else 1
nums = {A[0]: 1}
for i in range(1, N):
    hap.append(hap[i - 1] + A[i])
    if hap[i] == K:
        ans += 1
    target = hap[i] - K
    if target in nums:
        ans += nums[target]
    if hap[i] in nums:
        nums[hap[i]] += 1
    else:
        nums[hap[i]] = 1
print(ans)