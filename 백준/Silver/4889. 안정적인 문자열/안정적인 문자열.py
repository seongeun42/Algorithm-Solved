tc = 1
while tc:
    data = input()
    if '-' in data:
        break
    s = []
    cnt = 0
    for i in range(len(data)):
        if data[i] == '}':
            if not s:
                s.append('{')
                cnt += 1
            else:
                s.pop()
        else:
            s.append('{')
    if len(s) > 0:
        cnt += len(s) // 2
    print(f"{tc}. {cnt}")
    tc += 1