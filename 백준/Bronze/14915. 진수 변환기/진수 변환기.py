def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    return convert(q, base) + T[r] if q else T[r]

m, n = map(int, input().split())
print(convert(m, n))