def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

N, M = map(int, input().split())
if N == M == 0:
    print(0)
else:
    v = gcd(N, M)
    print(1 if v == 1 or v == -1 else 2)