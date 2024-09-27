s = input()
leng = len(s)
stack = []
isPPAP = False
i = 0
while i < leng:
    if s[i] == 'P':
        if i < leng - 4 and s[i:i+4] == "PPAP":
            stack.append("P")
            isPPAP = True
            i += 4
        elif stack and stack[-1] == 'P' and i < leng - 3 and s[i:i+3] == "PAP":
            isPPAP = True
            i += 3
        else:
            stack.append("P")
            isPPAP = False
            i += 1
    elif s[i] == "A":
        if len(stack) >= 2 and stack[-2] == "P" and stack[-1] == "P" and i < leng - 1 and s[i+1] == "P":
            stack.pop()
            isPPAP = True
            i += 2
        else:
            isPPAP = False
            break
print("PPAP" if isPPAP or s == "P" else "NP")