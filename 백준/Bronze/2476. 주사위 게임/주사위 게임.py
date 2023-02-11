N = int(input())
ans = 0
for _ in range(N):
    d = [*map(int, input().split())]
    if len(set(d)) == 1:
        ans = max(ans, 10000 + d[0] * 1000)
    elif len(set(d)) == 2:
        if d[0] == d[1] or d[0] == d[2]:
            ans = max(ans, 1000 + d[0] * 100)
        else:
            ans = max(ans, 1000 + d[1] * 100)
    else:
        ans = max(ans, max(d) * 100)
print(ans)