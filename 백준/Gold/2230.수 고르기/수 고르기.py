import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = sorted([int(input()) for _ in range(N)])
res = 2000000001
l, r = 0, 1
while l <= r and r < N:
    v = A[r] - A[l]
    if v >= M:
        res = min(res, v)
        l += 1
    else:
        r += 1
print(res)