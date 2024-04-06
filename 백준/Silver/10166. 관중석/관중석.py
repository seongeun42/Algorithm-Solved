from math import gcd
a, b = map(int, input().split())
arr = [[0] * (b + 1) for _ in range(b + 1)]
ans = 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
        g = gcd(i, j)
        arr[j // g][i // g] = 1
print(sum(map(sum, arr)))