N = int(input())
while 1:
    flag = 1
    for i in str(N):
        if i != '4' and i != '7':
            flag = 0
            N -= 1
    if flag:
        print(N)
        break