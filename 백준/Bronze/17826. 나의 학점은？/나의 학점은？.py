score = list(input().split())
h = score.index(input())
if h < 5:
    print("A+")
elif h < 15:
    print("A0")
elif h < 30:
    print("B+")
elif h < 35:
    print("B0")
elif h < 45:
    print("C+")
elif h < 48:
    print("C0")
else:
    print("F")