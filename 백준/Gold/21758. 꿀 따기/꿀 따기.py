N = int(input())
arr = [*map(int, input().split())]
psum = arr[:]
rpsum = arr[:]
for i in range(1, N):
    psum[i] = psum[i - 1] + arr[i]
    rpsum[N - i - 1] = rpsum[N - i] + arr[N - i - 1]
ans = 0
for i in range(1, N - 1):
    ans = max(ans, psum[i] - arr[0] + rpsum[i] - arr[-1])
for i in range(1, N - 1):
    ans = max(ans, psum[-1] - arr[0] - arr[i] + psum[-1] - psum[i])
for i in range(1, N - 1):
    ans = max(ans, rpsum[0] - arr[-1] - arr[i] + rpsum[0] - rpsum[i])
print(ans)