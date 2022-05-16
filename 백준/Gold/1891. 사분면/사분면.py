def sbmToCoordi(r, c, dep, size):
    if dep == d:
        return [r - y, c + x]

    if num[dep] == '1':
        return sbmToCoordi(r, c + size, dep + 1, size // 2)
    elif num[dep] == '2':
        return sbmToCoordi(r, c, dep + 1, size // 2)
    elif num[dep] == '3':
        return sbmToCoordi(r + size, c, dep + 1, size // 2)
    elif num[dep] == '4':
        return sbmToCoordi(r + size, c + size, dep + 1, size // 2)

def coordiToSbm(r, c, dep, size, num):
    if dep == d:
        print(num)
        return

    if mr < r + size:
        if mc < c + size:
            coordiToSbm(r, c, dep + 1, size // 2, num + '2')
        else:
            coordiToSbm(r, c + size, dep + 1, size // 2, num + '1')
    else:
        if mc < c + size:
            coordiToSbm(r + size, c, dep + 1, size // 2, num + '3')
        else:
            coordiToSbm(r + size, c + size, dep + 1, size // 2, num + '4')

d, num = input().split()
x, y = map(int, input().split())
d = int(d)
mr, mc = sbmToCoordi(0, 0, 0, 2 ** (d - 1))

if 0 <= mr < 2 ** d and 0 <= mc < 2 ** d:
    coordiToSbm(0, 0, 0, 2 ** (d - 1), '')
else:
    print(-1)