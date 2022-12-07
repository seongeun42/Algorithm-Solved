n = int(input())
ds = int(input())
c = sorted([int(input()) for _ in range(n - 1)], reverse=True)
ans = 0
while c and ds <= c[0]:
    ans += 1
    ds += 1
    c[0] -= 1
    c.sort(reverse=True)
print(ans)