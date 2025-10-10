n = int(input())
w = sorted([*map(int, input().split())])
ans = 200000
for i in range(n):
    v = w[i] + w[2 * n - i - 1] 
    if v < ans:
        ans = v
print(ans)