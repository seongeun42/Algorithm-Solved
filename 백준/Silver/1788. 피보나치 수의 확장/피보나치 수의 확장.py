n = int(input())
if n in [0, 1]:
    print(n, n, sep="\n")
else:
    pn = abs(n)
    pre, cur = 0, 1
    for i in range(2, pn + 1):
        pre, cur = cur, (pre + cur) % 1000000000
    print(1 if n > 0 or pn % 2 else -1)
    print(cur)