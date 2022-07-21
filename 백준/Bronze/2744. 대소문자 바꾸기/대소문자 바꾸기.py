s = input()
for c in s:
    print(c.upper() if 'a' <= c <= 'z' else c.lower(), end='')