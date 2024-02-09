N, M = map(int, input().split())
ans = 0
for i in range(N):
    if input().count('O') > M // 2:
        ans += 1
print(ans)