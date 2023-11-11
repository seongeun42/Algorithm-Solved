N, X = map(int, input().split())
A = [*map(int, input().split())]
ans = 2000000001
for i in range(1, N):
    v = X * (A[i - 1] + A[i])
    if ans > v:
        ans = v
print(ans)