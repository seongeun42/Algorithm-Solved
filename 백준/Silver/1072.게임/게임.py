X, Y = map(int, input().split())

win = Y * 100 // X

answer = 0
if win < 99:
    l, r = 1, X
    while l <= r:
        m = (l + r) // 2

        temp = (Y + m) * 100 // (X + m)
        if temp > win:
            r = m - 1
            answer = m
        else:
            l = m + 1

print(answer if answer > 0 else -1)