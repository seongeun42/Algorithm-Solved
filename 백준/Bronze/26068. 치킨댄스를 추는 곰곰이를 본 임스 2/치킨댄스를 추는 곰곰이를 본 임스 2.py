n = int(input())
ans = 0
for _ in range(n):
    if int(input()[2:]) <= 90:
        ans += 1
print(ans)