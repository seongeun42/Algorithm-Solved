n = int(input())
p = [*map(int, input().split())]
ans = 0
for i in range(3):
    ans += p[i] if p[i] <= n else n
print(ans)