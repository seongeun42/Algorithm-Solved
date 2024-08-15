N, K = map(int, input().split())
minimum = (1 + K) * K // 2
if N < minimum:
    print(-1)
else:
    cnt = [i for i in range(1, K + 1)]
    N -= minimum
    N %= K
    for i in range(1, N + 1):
        cnt[K - i] += 1
    print(cnt[-1] - cnt[0])