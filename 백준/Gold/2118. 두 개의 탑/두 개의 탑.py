import sys
input = sys.stdin.readline

N = int(input())
dist = [int(input()) for _ in range(N)]
pre_sum = [0] + dist[:]
for i in range(2, N + 1):
    pre_sum[i] += pre_sum[i - 1]
ans = 0
l, r = 0, 1
while l < N and r < N:
    d1 = pre_sum[r] - pre_sum[l]
    d2 = pre_sum[-1] - d1
    ans = max(ans, min(d1, d2))
    if d1 <= d2:
        r += 1
    else:
        l += 1
print(ans)