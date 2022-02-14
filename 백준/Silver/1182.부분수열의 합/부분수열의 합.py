from itertools import combinations
N, S = map(int, input().split())
nums = [*map(int, input().split())]
cnt = 0
for i in range(1, N + 1):
    for v in list(combinations(nums, i)):
        if sum(v) == S:
            cnt += 1
print(cnt)