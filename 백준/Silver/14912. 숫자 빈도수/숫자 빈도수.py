n, d = input().split()
n = int(n)
ans = 0
for i in range(1, n + 1):
    ans += str(i).count(d)
print(ans)