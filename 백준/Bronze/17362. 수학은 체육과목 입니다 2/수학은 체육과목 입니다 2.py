n = int(input()) - 2
if n <= 3:
    print(n + 2)
else:
    line = n // 4
    print(4 - (n % 4) if line % 2 else (n % 4) + 2)