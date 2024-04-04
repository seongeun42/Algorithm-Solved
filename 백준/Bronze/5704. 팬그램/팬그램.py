while True:
    s = input()
    ans = 'Y'
    if s == '*':
        break
    else:
        for c in range(97, 123):
            if s.find(chr(c)) == -1:
                ans = 'N'
                break
        print(ans)