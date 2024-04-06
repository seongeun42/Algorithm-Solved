from math import gcd

a, b = map(int, input().split())
arr = [[0] * b for _ in range(b)]
ans = 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
        g = gcd(i, j)
        x, y = i // g, j // g
        if not arr[x - 1][y - 1]:
            arr[x - 1][y - 1] = 1
            ans += 1
print(ans)