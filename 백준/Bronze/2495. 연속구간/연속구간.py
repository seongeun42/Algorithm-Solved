for _ in range(3):
    s = input()
    cnt = 1
    tmp = 1
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            tmp += 1
        else:
            cnt = max(cnt, tmp)
            tmp = 1
    cnt = max(cnt, tmp)
    print(cnt)