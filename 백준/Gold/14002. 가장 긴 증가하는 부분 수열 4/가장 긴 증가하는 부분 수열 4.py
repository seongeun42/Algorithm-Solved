N = int(input())
A = [*map(int, input().split())]
dp = [1] * N
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
leng = max(dp)
arr = []
print(leng)
for i in range(N - 1, -1, -1):
    if dp[i] == leng:
        arr.append(A[i])
        leng -= 1
print(*sorted(arr))