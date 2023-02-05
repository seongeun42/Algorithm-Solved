while 1:
    t = [*map(int, input().split())]
    if t[0] == 0:
        break
    ans = 1
    for i in range(1, len(t), 2):
        ans *= t[i]
        ans -= t[i + 1]
    print(ans)