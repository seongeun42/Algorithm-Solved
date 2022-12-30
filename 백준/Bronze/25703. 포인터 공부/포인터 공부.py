n = int(input())
print("int a;\nint *ptr = &a;")
star = "*"
for i in range(2, n + 1):
    star += "*"
    print("int ", star, "ptr", i, " = &ptr", sep="", end="")
    if i != 2: print(i - 1, end="")
    print(";")