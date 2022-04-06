n = [*map(int, input().split())]
i = min(n)
while 1:
    cnt = 0
    for v in n:
        if i % v == 0:
            cnt += 1
    if cnt >= 3:
        print(i)
        break
    i += 1