def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return abs(n1)

N, M = map(int, input().split())
if N == M == 0:
    print(0)
else:
    print(1 if gcd(N, M) == 1 else 2)