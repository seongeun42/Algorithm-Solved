def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

a, b = map(int, input().split())
print(a * b // gcd(a, b))
