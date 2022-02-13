N, C = map(int, input().split())
nums = [*map(int, input().split())]
cnt = {}
for i, v in enumerate(nums):
    if v in cnt:
        cnt[v][0] += 1
    else:
        cnt[v] = [1, i]
nums = sorted([[k, v[0], v[1]] for k, v in cnt.items()], key=lambda x:[-x[1], x[2]])
for v in nums:
    for _ in range(v[1]):
        print(v[0], end=' ')