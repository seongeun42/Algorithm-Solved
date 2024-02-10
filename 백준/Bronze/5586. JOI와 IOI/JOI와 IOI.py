s = input()
joi = ioi = 0
for i in range(3, len(s) + 1):
    if s[i - 3:i] == "JOI":
        joi += 1
    elif s[i - 3:i] == "IOI":
        ioi += 1
print(joi, ioi, sep="\n")