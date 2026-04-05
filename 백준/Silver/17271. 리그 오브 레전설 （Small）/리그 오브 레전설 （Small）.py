N, M = map(int, input().split())
max_b = N // M
MOD = 1_000_000_007
factorial = [1]
for i in range(1, N + 1):
    factorial.append(factorial[i - 1] * i)
ans = 0
for i in range(max_b + 1):
    a, b = N - (i * M), i
    ans += (factorial[a + b] // (factorial[a] * factorial[b])) % MOD
print(ans % MOD)