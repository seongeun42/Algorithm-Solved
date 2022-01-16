n, r, c = map(int, input().split())
res = 0
while n:
    n -= 1
    if r < 2 ** n and c >= 2 ** n:
        res += (2 ** n) ** 2 * 1
        c -= 2 ** n
    elif r < 2 ** n and c < 2 ** n:
        res += (2 ** n) ** 2 * 0
    elif r >= 2 ** n and c < 2 ** n:
        res += (2 ** n) ** 2 * 2
        r -= 2 ** n
    else:
        res += (2 ** n) ** 2 * 3
        r -= 2 ** n
        c -= 2 ** n
print(res)