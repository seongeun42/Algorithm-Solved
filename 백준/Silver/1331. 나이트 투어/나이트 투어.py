s = [input() for _ in range(36)]
v = {s[0]}
isOk = 1
for i in range(1, 36):
    al = abs(ord(s[i - 1][0]) - ord(s[i][0]))
    nu = abs(ord(s[i - 1][1]) - ord(s[i][1]))
    if s[i] in v or [al, nu] not in [[2, 1], [1, 2]]:
        isOk = 0
        break
    else:
        v.add(s[i])
al = abs(ord(s[0][0]) - ord(s[-1][0]))
nu = abs(ord(s[0][1]) - ord(s[-1][1]))
if [al, nu] not in [[2, 1], [1, 2]] or not isOk:
    print("Invalid")
else:
    print("Valid")