cn = int(input())
n = 1
while cn != 1:
    if cn % 2 == 1:
        cn = 3 * cn + 1
    else:
        cn //= 2
    n += 1
print(n)