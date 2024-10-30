N = int(input())
ans = 0
for i in range(1, N + 1):
    if i % sum(map(int, list(str(i)))) == 0:
        ans += 1
print(ans)