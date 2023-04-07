n = int(input())
a = "* " * n
b = " *" * n
for i in range(n):
    print(b if i % 2 else a)