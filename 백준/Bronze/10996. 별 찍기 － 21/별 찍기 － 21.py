def star(s):
    print("* " * ((s - 1) // 2 + 1))
    if s > 1:
        print(" *" * (s // 2))

n = int(input())
for _ in range(n):
    star(n)