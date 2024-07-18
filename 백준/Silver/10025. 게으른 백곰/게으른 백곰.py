N, K = map(int, input().split())
arr = [0] * 1000001
for _ in range(N):
    g, x = map(int, input().split())
    arr[x] = g
ans = sum(arr[:2 * K + 1])
cnt = ans
for i in range(K + 1, 1000001 - K):
    cnt -= arr[i - K - 1]
    cnt += arr[i + K]
    ans = max(ans, cnt)
print(ans)