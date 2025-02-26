while 1:
    n = int(input())
    if n == 0:
        break
    print(sum([(n - i + 1) ** 2 for i in range(1, n + 1)]))