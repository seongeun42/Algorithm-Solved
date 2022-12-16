a = [*map(int, input().split())]
r = [*map(int, input().split())]
ans = 0
for i in range(3):
    if a[i] - r[i] < 0:
        ans += r[i] - a[i]
print(ans)