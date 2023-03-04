n = [*map(int, input().split())]
while 1:
    for i in range(4):
        if n[i] > n[i + 1]:
            n[i], n[i + 1] = n[i + 1], n[i]
            print(*n)
    if n == sorted(n):
        break