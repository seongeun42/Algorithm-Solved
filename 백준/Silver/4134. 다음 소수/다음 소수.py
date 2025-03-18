T = int(input())
for _ in range(T):
    n = int(input())
    i = n
    while 1:
        if i <= 2:
            i = 2
            break
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            break
        i += 1
    print(i)