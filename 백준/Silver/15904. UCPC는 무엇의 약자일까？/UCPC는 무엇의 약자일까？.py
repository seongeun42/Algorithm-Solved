s = input()
ucpc = "UCPC"
i = 0
for c in s:
    if c == ucpc[i]:
        i += 1
        if i == 4: break
print("I love UCPC" if i == 4 else "I hate UCPC")