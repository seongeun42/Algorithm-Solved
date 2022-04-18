N, M = map(int, input().split())
left, right = [], []
for v in [*map(int, input().split())]:
    if v < 0:
        left.append(abs(v))
    else:
        right.append(v)
left.sort(reverse=True)
right.sort(reverse=True)
res = 0
for i in range(0, len(left), M):
    res += left[i] * 2
for i in range(0, len(right), M):
    res += right[i] * 2
if left and right:
    res -= left[0] if left[0] > right[0] else right[0]
elif left:
    res -= left[0]
elif right:
    res -= right[0]
print(res)