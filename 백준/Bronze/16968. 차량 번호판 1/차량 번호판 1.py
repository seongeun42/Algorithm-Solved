t = input()
ans = 10 if t[0] == 'd' else 26
for i in range(1, len(t)):
    if t[i] == 'c':
        v = 26 if t[i - 1] != 'c' else 25
    else:
        v = 10 if t[i - 1] != 'd' else 9
    ans *= v
print(ans)