def covert(n, d):
    res = []
    while n > 0:
        res.append(n % d)
        n //= d
    return res[::-1]

a, b = map(int, input().split())
m = int(input())
num = [*map(int, input().split())]
ten = sum([num[m - i - 1] * (a ** i) for i in range(m)])
print(*covert(ten, b))