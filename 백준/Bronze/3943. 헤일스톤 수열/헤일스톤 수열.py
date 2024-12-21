from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    arr = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        arr.append(n)
    print(max(arr))