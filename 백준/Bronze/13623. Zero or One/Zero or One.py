a, b, c = input().split()
if a == b == c:
    print("*")
elif a == b:
    print("C")
elif a == c:
    print("B")
else:
    print("A")