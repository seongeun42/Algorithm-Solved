n = sorted([*map(int, input().split())])
s = input()
o = {"A": 0, "B": 1, "C": 2}
for i in range(3):
    print(n[o[s[i]]], end=" ")