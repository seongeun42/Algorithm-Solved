import math

a, b = map(int, input().split())
gcd = math.gcd(a, b)
for i in range(1, gcd + 1):
    if gcd % i == 0:
        print(i, a // i, b // i)