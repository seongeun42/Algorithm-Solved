n, K = map(int, input().split())
ans = 0
t = int(input())
for _ in range(n - 1) :
    tmp = int(input())
    if t - tmp >= K : ans += 1
    t = tmp
print(ans)