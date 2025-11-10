N = int(input())
A = [*map(int, input().split())]
desc = [1] * N
asc = [1] * N
desc[0], asc[-1] = 1, 1
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i] and desc[i] <= desc[j]:
            desc[i] = desc[j] + 1
        if A[N - j - 1] < A[N - i - 1] and asc[N - i - 1] <= asc[N - j - 1]:
            asc[N - i - 1] = asc[N - j - 1] + 1
ans = 0
for i in range(N):
    leng = desc[i] + asc[i]
    if ans < leng:
        ans = leng
print(ans - 1)