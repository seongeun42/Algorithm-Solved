L = int(input())
v, m = divmod(L, 5)
print(v + 1 if m != 0 else v)