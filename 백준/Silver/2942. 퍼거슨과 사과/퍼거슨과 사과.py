import math

r, g = map(int, input().split())
x = math.gcd(r, g)
ans = set([])
for i in range(1, int(x**0.5) + 1):
    if x % i == 0:
        ans.add(i)
        ans.add(x // i)
for i in ans:
    print(i, r // i , g // i)