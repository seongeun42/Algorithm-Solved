n = int(input()) - 1
ans = 4
for i in range(n + 1):
    c = 2 ** i
    ans += 5 + (4 * (c - 1) * 2) + (3 * ((c - 1) ** 2))
print(ans)