N, K = map(int, input().split())
ans = 0
for i in range(1, K + 1):
    v = int(str(N * i)[::-1])
    if ans < v:
        ans = v
print(ans)