score = [int(input()) for _ in range(6)]

a = sum([score[i] * (3 - i) for i in range(3)])
b = sum([score[i] * (3 - (i % 3)) for i in range(3, 6)])

if a > b: print("A")
elif b > a: print("B")
else: print("T")