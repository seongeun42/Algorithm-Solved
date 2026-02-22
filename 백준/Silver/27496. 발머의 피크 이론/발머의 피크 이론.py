N, L = map(int, input().split())
a = [*map(int, input().split())]
prefix_sum = [0]
ans = 0
for i, v in enumerate(a):
    prefix_sum.append(prefix_sum[-1] + v)
    if i >= L:
        prefix_sum[-1] -= a[i - L]
    if 129 <= prefix_sum[-1] <= 138:
        ans += 1
print(ans)