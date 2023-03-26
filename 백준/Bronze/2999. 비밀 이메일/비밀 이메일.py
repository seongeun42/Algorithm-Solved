s = input()
r, c = 1, len(s)
while r < c:
    r += 1
    if len(s) % r == 0:
        c = len(s) // r
print("".join([s[i::c] for i in range(c)]))