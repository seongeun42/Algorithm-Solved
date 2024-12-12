n = int(input())
pre, cur = 0, 1
if n <= 1:
    print(n)
else:
    for i in range(n - 1):
        cur, pre = (cur + pre) % 1000000007, cur
    print(cur)