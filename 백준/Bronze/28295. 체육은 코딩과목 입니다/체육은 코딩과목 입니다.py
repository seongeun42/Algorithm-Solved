ans = 0
d = ["N", "E", "S", "W"]
for _ in range(10):
    c = input()
    if c == "1":
        ans = (ans + 1) % 4
    elif c == "2":
        ans = (ans + 2) % 4
    else:
        ans = (ans - 1) % 4
print(d[ans])