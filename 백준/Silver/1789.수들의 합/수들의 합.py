s = int(input())
i, res = 2, 1
while 1:
    if res <= s < res + i:
        print(i - 1)
        break
    res += i
    i += 1