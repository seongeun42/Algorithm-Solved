while 1:
    n = input()
    if n == "0": break
    ans = 1
    for v in n:
        if v == "0":
            ans += 5
        elif v == "1":
            ans += 3
        else:
            ans += 4
    print(ans)