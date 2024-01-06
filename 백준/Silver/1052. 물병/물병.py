N, K = map(int, input().split())
ans = 0
while bin(N).count('1') > K:
    v = 2 ** bin(N)[::-1].index('1')
    ans += v
    N += v
print(ans)