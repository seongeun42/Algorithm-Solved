stroke = "32123323322122122212111221"
A = ord("A")
jm, her = input(), input()
s = []
for i in range(len(jm)):
    s.append(int(stroke[ord(jm[i]) - A]))
    s.append(int(stroke[ord(her[i]) - A]))
for i in range(len(s) - 1, 1, -1):
    for j in range(i):
        s[j] = (s[j] + s[j + 1]) % 10
print(*s[:2], sep="")