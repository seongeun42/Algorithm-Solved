e, s, m = map(int, input().split())
res = e
while 1:
    if res % 28 == s % 28 and res % 19 == m % 19:
        print(res)
        break
    res += 15