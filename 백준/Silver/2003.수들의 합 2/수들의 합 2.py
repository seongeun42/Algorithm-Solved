N, M = map(int, input().split())
A = [*map(int, input().split())]
l, r = 0, 1
cnt = 0
while l <= r and r <= N:
    v = sum(A[l:r])
    if v == M:
        cnt += 1
        r += 1
    elif v < M:
        r += 1
    else:
        l += 1
print(cnt)