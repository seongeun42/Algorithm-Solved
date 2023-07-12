a = []
for i in range(5):
    if "FBI" in input():
        a.append(i + 1)
if len(a): print(*a)
else: print("HE GOT AWAY!")