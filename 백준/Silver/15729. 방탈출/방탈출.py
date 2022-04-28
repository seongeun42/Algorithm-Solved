N = int(input())
B = [*map(int, input().split())]
C = [0] * N
res = 0
for i in range(N):
    if B[i] != C[i]:
        C[i] = not C[i]
        if i < N - 1:
            C[i + 1] = not C[i + 1]
        if i < N - 2:
            C[i + 2] = not C[i + 2]
        res += 1
print(res)