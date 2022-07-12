while 1:
    try:
        strs = input()
        s, b, n, space = 0, 0, 0, 0
        for c in strs:
            if 'A' <= c <= 'Z':
                b += 1
            elif 'a' <= c <= 'z':
                s += 1
            elif '0' <= c <= '9':
                n += 1
            elif c == ' ':
                space += 1
        print(s, b, n, space)
    except: break