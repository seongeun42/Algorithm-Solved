def gcd(n, m):
    while m:
        n, m = m, n % m
    return n

N, M = map(int, input().split())
print(M - gcd(N, M))