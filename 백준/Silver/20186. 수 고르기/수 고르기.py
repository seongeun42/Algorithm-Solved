from itertools import combinations

N, K = map(int, input().split())
nums = [*map(int, input().split())]
ans = 0
for cb in combinations(range(N), K):
    v = 0
    for i, idx in enumerate(cb):
        v += nums[idx] - i
    if ans < v:
        ans = v
print(ans)