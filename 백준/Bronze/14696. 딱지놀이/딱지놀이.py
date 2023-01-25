n = int(input())
for _ in range(n):
    a = input().split()[1:]
    b = input().split()[1:]
    a4, a3, a2, a1 = a.count("4"), a.count("3"), a.count("2"), a.count("1")
    b4, b3, b2, b1 = b.count("4"), b.count("3"), b.count("2"), b.count("1")
    if a4 != b4:
        print("A" if a4 > b4 else "B")
    elif a3 != b3:
        print("A" if a3 > b3 else "B")
    elif a2 != b2:
        print("A" if a2 > b2 else "B")
    elif a1 != b1:
        print("A" if a1 > b1 else "B")
    else:
        print("D")