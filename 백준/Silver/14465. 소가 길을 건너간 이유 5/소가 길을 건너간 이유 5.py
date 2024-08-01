import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())
signal = [1] * (N + 1)
for _ in range(B):
    signal[int(input())] = 0
prefix = sum(signal[1:K+1])
ans = K - prefix
for i in range(K + 1, N + 1):
    prefix -= signal[i - K]
    prefix += signal[i]
    need = K - prefix
    if ans > need:
        ans = need
print(ans)