s = input()
t = 1
z = 1 if s[0] == '0' else 0
c = s[0]
for v in s:
    if v != c:
        c = v
        t += 1
        if v == '0':
            z += 1
print(min(z, t - z))