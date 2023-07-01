n = int(input())
k = int(input())
if n <= 60:
    print(n * 1500)
else:
    e = max(n - 60 - k, 0)
    print((n - e) * 1500 + e * 3000)