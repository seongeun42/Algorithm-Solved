n = int(input())
s = input()
A = s.count("A")
B = n - A
if A == B:
    print("Tie")
else:
    print("A" if A > B else "B")