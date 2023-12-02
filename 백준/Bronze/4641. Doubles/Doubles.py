while 1:
    n = [*map(int, input().split())]
    if len(n) == 1 and n[0] == -1:
        break
    num = [0] * 201
    ans = 0
    for i in range(len(n) - 1):
        num[n[i]] = 1
    for i in range(len(n) - 1):
        if num[n[i] * 2] == 1:
            ans += 1
    print(ans)