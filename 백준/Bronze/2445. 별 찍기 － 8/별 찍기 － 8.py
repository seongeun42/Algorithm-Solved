n = int(input())
for i in range(1, n + 1):
    s = "*" * i + " " * (n - i)
    print(s, s[::-1], sep="")
for i in range(n - 1, 0, -1):
    s = "*" * i + " " * (n - i)
    print(s, s[::-1], sep="")