def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

n, m = map(int, input().split(':'))
d = gcd(n, m)
print(n // d, ":", m // d, sep='')