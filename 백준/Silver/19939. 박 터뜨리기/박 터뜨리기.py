N, K = map(int, input().split())
minimum = (1 + K) * K // 2
if N < minimum:
    print(-1)
else:
    cnt = [i for i in range(1, K + 1)]
    N -= minimum
    N %= K
    print(cnt[-1] - cnt[0] + (1 if N > 0 else 0))