while 1:
    try:
        n = int(input())
        ans = 1
        while 1:
            if ans % n == 0:
                print(len(str(ans)))
                break
            ans = ans * 10 + 1
    except EOFError:
        break