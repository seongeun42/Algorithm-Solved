num = input()
ans = 1
i = 0
while 1:
    for c in str(ans):
        if num[i] == c:
            i += 1
            if i >= len(num):
                print(ans)
                exit()
    ans += 1