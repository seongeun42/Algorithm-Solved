def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
bm = (b1 * b2) // gcd(b1, b2)
bj = (a1 * (bm // b1)) + (a2 * (bm // b2))
ngcd = gcd(bm, bj)
print(bj // ngcd, bm // ngcd)