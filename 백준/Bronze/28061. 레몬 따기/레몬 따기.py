N = int(input())
a = [*map(int, input().split())]
ans = 0
for i, v in enumerate(a):
    v = max(0, v - (N - i))
    if ans < v:
        ans = v
print(ans)