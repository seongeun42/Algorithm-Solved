n = int(input())
x = sorted([*map(int, input().split())])
ans = 0
for i in range(n):
    ans += x[i] * i - sum(x[:i])
    ans += sum(x[i+1:]) - x[i] * (n - i - 1)
print(ans)