while 1:
    s = input()
    if s == "#":
        break
    print(f'{s[0]} {s.lower().count(s[0]) - 1}')