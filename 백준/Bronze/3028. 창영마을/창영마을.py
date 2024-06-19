s = input()
ans = 1
for c in s:
    if c == 'A':
        if ans == 1:
            ans = 2
        elif ans == 2:
            ans = 1
    elif c == 'B':
        if ans == 2:
            ans = 3
        elif ans == 3:
            ans = 2
    elif c == 'C':
        if ans == 1:
            ans = 3
        elif ans == 3:
            ans = 1
print(ans)