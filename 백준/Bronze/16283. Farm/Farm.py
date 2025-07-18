a, b, n, w = map(int, input().split())
is_exist = False
ans = []
for i in range(1, n):
    v = a * i + b * (n - i)
    if w == v:
        if not is_exist:
            ans = [i, n - i]
            is_exist = True
        else:
            ans = []
if ans:
    print(*ans)
else:
    print(-1)